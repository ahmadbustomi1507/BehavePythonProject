
from requests import *
import json


# Request Builder
def Send_Request(type= "GET", api_endpoint =None, Params =None , Body={} ):
    if type =='GET':
        response = get(url=api_endpoint, params=Params)
    elif type == 'POST' :
        response = post(url=api_endpoint,  data = Body)
        pass

    return response

# Parsing the JSON from external
def json2dict(input_json={}):
    return json.loads(input_json)


def dict2json(input_dict={}):
    return json.dumps(input_dict)

