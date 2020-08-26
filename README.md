# Solidarity Map API

This project implements the database / API backend for the [Solidarity Map](https://github.com/allout/solidarity-map) project

## Setup

This project is written in Python and based on the [Python Eve](https://docs.python-eve.org/en/stable/) project, which uses the [Python Flask](https://palletsprojects.com/p/flask/) project at its core.

It requires connection to a Mongo database.

All options can be configured via the following environment variables:

- MONGODB_URI:

  the database connection string, eg `mongodb://localhost:27017`

- X_DOMAINS

  a comma-separated list of domains that should be allowed to make requests of this service (ie at least the domain of where your Solidarity Map project is running)

- API_USER

  The api username allowed to write to the database (default: `api`)

- API_PASSWORD

  The accompanying password for the above user

- RECAPTCHA_ENABLED

  Default is disabled. If given the value of `1` this is enabled and a recaptcha will be used to further protect submissions to the website from spamming. This option must be enabled on the frontend Solidarity Map app as well in order to work.

- RECAPTCHA_SECRET_KEY

  Required if the above is enabled

- LOG_LEVEL

  The verboseness of the server log. Options are `DEBUG`, `INFO`, `WARNING`, `ERROR`. Defaults to `INFO`

## Deployment

This project is already set up to be deployed to Heroku, but could be hosted on anything that can run a Python WSGI application.
