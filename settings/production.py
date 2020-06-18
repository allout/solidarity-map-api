import os
from environs import Env
from base import *

env = Env()

# DB connection
MONGO_URI = env.str('MONGO_URI')

# CORS whitelist for client domains.
# This can be an env var which contains a comma separated list of domains allowed to make requests of this server
X_DOMAINS = env.list('X_DOMAINS', default=[])
print(X_DOMAINS)
