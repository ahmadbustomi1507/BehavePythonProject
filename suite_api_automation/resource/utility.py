import json

def string2dict(json_string:str):
    # sample json_string
    # x =  '{ "name":"John", "age":30, "city":"New York"}'
    return json.loads(json_string)

def dict2json(dict_input:dict):

    return json.dumps(dict_input)