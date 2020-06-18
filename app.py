#!/usr/bin/env python
import bcrypt
import importlib
import os
import sys
from eve import Eve, auth
from hashlib import sha256

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_PATH, 'settings'))
EVE_SETTINGS = os.environ.get('EVE_SETTINGS', 'settings/local.py')
EVE_SETTINGS_ROOT, _ = os.path.splitext(EVE_SETTINGS)
EVE_SETTINGS_PROFILE = os.path.basename(EVE_SETTINGS_ROOT)
ABS_SETTINGS_PATH = os.path.join(CURRENT_PATH, EVE_SETTINGS)

# Allow current settings to be available to this code
settings = importlib.import_module(f'settings.{EVE_SETTINGS_PROFILE}')


class BasicAuth(auth.BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == settings.API_USER and password == settings.API_PASSWORD


def get_eve_app():
    """
    Initializes Eve app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    return Eve(settings=ABS_SETTINGS_PATH, auth=BasicAuth)


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_eve_app()
    app.run(debug=True)
