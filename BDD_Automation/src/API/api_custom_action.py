
from tools.Utility import *
from tools import Definition as Define

'''
Description 
    Custom action, example    
    
    # {
    # 	"action": "RESETBALANCE",
    # 	"param": [
    # 		{
    # 			"paramname": "MSISDN",
    # 			"paramvalue": "6281808030805"
    # 		},
    # 		{
    # 			"paramname": "BALANCE",
    # 			"paramvalue": "50000"
    # 		},
    # 		{
    # 			"paramname": "TYPE",
    # 			"paramvalue": "MO"
    # 		}
    # 	]
    #
    # }
    # {
    # 	"action": "RESETBALANCE",
    # 	"param": [
    # 		{
    # 			"paramname": "MSISDN",
    # 			"paramvalue": "628176677807"
    # 		},
    # 		{
    # 			"paramname": "BALANCE",
    # 			"paramvalue": "1000000"
    # 		},
    # 		{
    # 			"paramname": "TYPE",
    # 			"paramvalue": "PO"
    # 		}
    # 	]

'''

# API Endpoint
# API_CUSTOM_ACTION_ENDPOINT = IP_ENV_SIT3 + 'custom-action'

# Request Builder
def API_CUSTOM_ACTION_ENDPOINT(env=None, params ):
    response = Send_Request(type= "GET", api_endpoint =env + Define.API_CUSTOM_ACTION, Params =params)
    return response
