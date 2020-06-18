#!/usr/bin/env python
import os
import sys
from eve import Eve

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, 'settings'))


def get_eve_app():
    """
    Initializes Eve app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    EVE_SETTINGS = os.environ.get('EVE_SETTINGS', 'settings/local.py')
    abs_settings_path = os.path.join(current_path, EVE_SETTINGS)
    return Eve(settings=abs_settings_path)


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_eve_app()
    app.run(debug=True)
