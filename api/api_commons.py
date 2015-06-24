import endpoints


WEB_CLIENT_ID = 'replace this with your Android client ID'
ANDROID_CLIENT_ID = 'replace this with your Android client ID'
IOS_CLIENT_ID = 'replace this with your iOS client ID'
ANDROID_AUDIENCE = WEB_CLIENT_ID


capitolbells = endpoints.api(name='capitolbells', version='v1.0',
                             allowed_client_ids=[WEB_CLIENT_ID, ANDROID_CLIENT_ID, IOS_CLIENT_ID,
                                                 endpoints.API_EXPLORER_CLIENT_ID],
                             audiences=[ANDROID_AUDIENCE],
                             scopes=[endpoints.EMAIL_SCOPE])