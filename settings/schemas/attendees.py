schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'lat': {'type': 'number', 'min': -90, 'max': 90},
    'lng': {'type': 'number', 'min': -180, 'max': 180},
    'firstName': {'type': 'string', 'minlength': 0, 'maxlength': 100,},
    'lastName': {'type': 'string', 'minlength': 0, 'maxlength': 100,},
    'subscriptionCountry': {'type': 'string', 'minlength': 2, 'maxlength': 2},
    'solidarityCountry': {'type': 'string', 'minlength': 0, 'maxlength': 2},
    'emojiIndices': {'type': 'list'},
}

attendees = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'attendee',
    # 'additional_lookup': {
    #     'url': 'regex("[\w]+")',
    #     'field': 'lastname'
    # },
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH', 'PUT'],
    'schema': schema,
}
