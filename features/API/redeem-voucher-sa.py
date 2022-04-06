
from features.tools.Utility import *

'''
Description 
    Redeem SA Voucher with params as below:
    PARAMS = {
        'DEALERMSISDN':'628176677807',
        'HRN'         :'4678009180739283',
        'MSISDN'      :'628176677807',
        'USERINPUT'   : '6281808030805'
    }
    
    example : 'http://redeem-voucher-sa-sit.api.devgcp.excelcom.co.id/umb/menu/business/transferSa' ?' +
                             'DEALERMSISDN=628176677807 ' +
                             '&HRN=4678009180739283' +
                             '&MSISDN=628176677807&USERINPUT=6281808030805
    
'''

# API Endpoint
API_REDEEM_VOUCHER_SA_ENDPOINT = 'http://redeem-voucher-sa-sit.api.devgcp.excelcom.co.id/umb/menu/business/transferSa'

# Request Builder
def API_REDEEM_VOUCHER_SA_ENDPOINT(api = None, params=None ):
    response = Send_Request(type= "GET", api_endpoint =api, Params =params)
    return response
