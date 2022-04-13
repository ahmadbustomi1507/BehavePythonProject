
from tools import Definition as Define
import httpx
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


# Params = {
#     'DEALERMSISDN': '628176677807',
#     'HRN': '4678009180739283',
#     'MSISDN': '628176677807',
#     'USERINPUT': '6281808030805'
# }
import httpx

async def main(env=None,Params):
    async with httpx.AsyncClient() as client:
        response = await client.get(Define.API_REDEEM_VOUCHER_SA_ENDPOINT,params =Params)
        return response
