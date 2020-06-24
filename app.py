#!/usr/bin/env python
import importlib
import json
import os
import requests
import sys
from eve import Eve, auth
from flask import abort
from hashlib import sha256

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


def recaptcha_hook(resource_name, items, original=None):
    for item in items:
        response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            {
                'response': item.pop('gRecaptchaResponse', None),
                'secret': imported_settings.RECAPTCHA_SECRET_KEY,
            },
        )
        response_text = json.loads(response.text)
        if not response_text['success']:
            print(response_text)
            abort(403)
            break


def get_eve_app():
    """
    Initializes Eve app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    app = Eve(settings=ABS_SETTINGS_PATH, auth=BasicAuth)
    if imported_settings.RECAPTCHA_ENABLED:
        app.on_insert = recaptcha_hook
        app.on_replace = recaptcha_hook
        app.on_update = recaptcha_hook
    return app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_eve_app()
    app.run(debug=True)
