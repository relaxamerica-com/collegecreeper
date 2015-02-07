from google.appengine.api.app_identity import get_application_id

app_name = get_application_id()

COLLEGES = {
    'collegecreepermatt': {
        'fdu': {
            'latitude': 40.776479,
            'longitude': -74.433242,
        },
        'msu': {
            'latitude': 40.86152,
            'longitude': -74.198552,
        },
    }
}[app_name]


ANALYTICS = {
    'collegecreepermatt': {
        'GOOGLE_ANALYTICS_CODE': 'UA-59471096-1'
    }
}[app_name]


INSTAGRAM = {
    'collegecreepermatt': {
        'POLLING_ENABLED': True,
        'ACCESS_TOKEN': '1422127379.5a3e9d7.bb8d3627019f4ab1bd07d04322e373d1',
        'CLIENT_ID': '5a3e9d750ad54c6aa747c5e428e91791',
        'CLIENT_SECRET': 'bf49c41ca29a4070a434143d2a5c6d97',
    },
}[app_name]
