
API_CUSTOM_ACTION_ENDPOINT = IP_ENV_SIT3 + 'custom-action'
from resource.build_request import *

# Request Builder
def API_REDEEM_VOUCHER_SA_ENDPOINT(api_endpoint, params ):
    create_new_request = build_request(api_endpoint)
    response = Send_Request(type= "GET", api_endpoint =api_endpoint, Params =params)
    return response
