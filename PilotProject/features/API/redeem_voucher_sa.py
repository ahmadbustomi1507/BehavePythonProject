
# from tools.Utility import *

# from Utility import Send_Request
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

# API Endpoint
API_REDEEM_VOUCHER_SA_ENDPOINT = 'http://redeem-voucher-sa-sit.api.devgcp.excelcom.co.id/umb/menu/business/transferSa'

# Request Builder
# def API_REDEEM_VOUCHER_SA(params=None ):
#     response = Send_Request(type= "GET", api_endpoint =API_REDEEM_VOUCHER_SA_ENDPOINT, Params =params)
#     return response

Params = {
    'DEALERMSISDN': '628176677807',
    'HRN': '4678009180739283',
    'MSISDN': '628176677807',
    'USERINPUT': '6281808030805'
}
# res = API_REDEEM_VOUCHER_SA(Params)
# print(res.text)
# response = httpx.request('GET', API_REDEEM_VOUCHER_SA_ENDPOINT,params =Params)
# print(response )
# async with httpx.AsyncClient() as client:
#      r = await client.get(API_REDEEM_VOUCHER_SA_ENDPOINT,params =Params)
#      print(r)
#      client.close()

# import asyncio
import httpx

async def API_REDEEM_VOUCHER_SA():
    async with httpx.AsyncClient() as client:
        response = await client.get(API_REDEEM_VOUCHER_SA_ENDPOINT,params =Params)
        return response
        # print(response)
        # print(response.text)

# asyncio.run(main())
