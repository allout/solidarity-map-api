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
    # init eve
    eve_app = Eve(settings=os.environ.get('EVE_SETTINGS_FILE', 'settings/local.py'))
    return eve_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_eve_app()
    app.run(debug=True)
