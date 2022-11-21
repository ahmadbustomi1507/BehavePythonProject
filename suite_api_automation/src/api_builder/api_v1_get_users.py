
from resource.build_request import *

'''
    Path :  /api/v1/users
    Desc : this API is used to get all the users data available from database
'''
def api_get_users(base_url:str,path:str,payload:dict,params:dict = None):
    request = build_request(base_url=base_url,resource_path=path)
    request.add_payload_dict(payload)
    # request.add_params(params)
    response = request.send_request("GET")
    return response