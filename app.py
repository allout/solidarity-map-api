#!/usr/bin/env python
import importlib
import json
import logging
import os
import requests
import sys
from eve import Eve, auth
from flask import abort
from hashlib import sha256

logging.basicConfig()
logger = logging.getLogger(__name__)

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_PATH, 'settings'))
EVE_SETTINGS = os.environ.get('EVE_SETTINGS', 'settings/local.py')
EVE_SETTINGS_ROOT, _ = os.path.splitext(EVE_SETTINGS)
EVE_SETTINGS_PROFILE = os.path.basename(EVE_SETTINGS_ROOT)
ABS_SETTINGS_PATH = os.path.join(CURRENT_PATH, EVE_SETTINGS)

# Allow current settings to be available to this code
imported_settings = importlib.import_module(f'settings.{EVE_SETTINGS_PROFILE}')


class BasicAuth(auth.BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return (
            username == imported_settings.API_USER
            and password == imported_settings.API_PASSWORD
        )


def recaptcha_hook(resource, request, lookup=None):
    recaptcha_payload = {
        'response': request.json.pop('gRecaptchaResponse', None),
        'secret': imported_settings.RECAPTCHA_SECRET_KEY,
    }
    logger.debug(recaptcha_payload)
    recaptcha_response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify', recaptcha_payload,
    )
    response_text = json.loads(recaptcha_response.text)
    if not response_text['success']:
        logger.debug(response_text)
        abort(403)


def get_eve_app():
    """
    Initializes Eve app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    app = Eve(settings=ABS_SETTINGS_PATH, auth=BasicAuth)
    if imported_settings.RECAPTCHA_ENABLED:
        app.on_pre_POST = recaptcha_hook
        app.on_pre_PATCH = recaptcha_hook
        app.on_pre_PUT = recaptcha_hook
    return app


app = get_eve_app()


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    logger.setLevel(logging.DEBUG)
    app.run(debug=True)
