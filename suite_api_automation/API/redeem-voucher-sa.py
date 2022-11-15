
from features.tools.Utility import *
from features.tools.Definition import *
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


# Request Builder
def API_REDEEM_VOUCHER_SA_ENDPOINT( params=None ):
    response = Send_Request(type= "GET", api_endpoint =API_REDEEM_VOUCHER_SA_ENDPOINT, Params =params)
    return response
