
import requests import *
# API Endpoint
API_REDEEM_VOUCHER_SA_ENDPOINT = 'http://redeem-voucher-sa-sit.api.devgcp.excelcom.co.id/umb/menu/business/transferSa'

# Request Builder
def Send_Request(type= "GET", api_endpoint =None, Params =None , Body={} ):
    if type =='GET':
        response = get(url=api_endpoint, params=Params)
    elif type == 'POST' :
        response = post(url=api_endpoint,  data = Body)
        pass

    return response