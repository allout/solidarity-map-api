import os
from environs import Env

from schemas.attendees import attendees

env = Env()

URL_PREFIX = 'api'
API_VERSION = 'v1'

DOMAIN = {'attendees': attendees}

MONGO_DBNAME = 'solidarity-map'

# Auth
# Make sure these are set as environment vars in production.
# Using the defaults here is not secure!
API_USER = env.str('API_USER', default='api')
API_PASSWORD = env.str('API_PASSWORD', default='JY9^QUfNt}+HuDfgvJ62')

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
# RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
# ITEM_METHODS = ['GET', 'PATCH', 'PUT']
