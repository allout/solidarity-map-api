import os
from base import *

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
