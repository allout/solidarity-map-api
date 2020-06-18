import os

from schemas.attendees import attendees

URL_PREFIX = 'api'
API_VERSION = 'v1'

DOMAIN = {'attendees': attendees}

MONGO_DBNAME = 'solidarity-map'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
# RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
# ITEM_METHODS = ['GET', 'PATCH', 'PUT']
