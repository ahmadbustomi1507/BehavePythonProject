
import httpx
from tools import Definition as Define


'''
example params 
{
    'msisdn' :'6287875736063',
    'allowCancel' : 'N'
}


'''
# Request Builder
def API_SUBSCRIBER_PROFILE_INFO_ENDPOINT(env=None, params):
    # response = Send_Request(type="GET", api_endpoint=env + Define.API_AMDOCS_CM_SUBSCRIBER_INFO, Params=params)
    return httpx.get(url=env + Define.API_SUBSCRIBER_PROFILE_INFO,
                     params=Params,headers={
                        'accept' : '*/*'
                    })



