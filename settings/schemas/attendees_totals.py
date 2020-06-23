attendees_totals = {
    'url': 'attendees/totals',
    'datasource': {
        'source': 'attendees',
        'aggregation': {
            'pipeline': [
                {
                    '$facet': {
                        'countries': [
                            {'$group': {'_id': '$solidarityCountry'},},
                            {'$count': 'total'},
                        ],
                        'attendees': [{'$count': 'total'},],
                    }
                }
            ]
        },
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=120',
    'cache_expires': 120,
}
