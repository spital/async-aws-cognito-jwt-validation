# coding=utf-8

import cognitojwt

id_token = '<YOUR_TOKEN_HERE>'
REGION = '**-****-*'
USERPOOL_ID = 'eu-west-1_*******'
APP_CLIENT_ID = '1p3*********'


# Async mode
verified_claims: dict = await cognitojwt.decode_async(
    id_token,
    REGION,
    USERPOOL_ID,
    app_client_id=APP_CLIENT_ID,  # Optional
    testmode=True  # Disable token expiration check for testing purposes
)
