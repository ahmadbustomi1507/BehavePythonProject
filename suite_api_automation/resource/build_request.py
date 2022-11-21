from typing import Dict,Any
import httpx
class build_request(object):
    def __init__(self, base_url:str, resource_path:str):
        #ex domain:
        # www.ninjaapi.com
        self.base_url = base_url

        #ex url:
        # /api/v2/jne/get_location
        self.resource_path      = resource_path
        self.payload       = dict()
        self.params        = dict()
        self.headers       = {
            "Accept":"*/*",
            "Connection":"keep-alive",
            "Content-Type":"application/json"
        }

    # on progress
    def add_headers(self,dict_headers):
        for key in dict_headers.keys():
            self.headers[key] = dict_headers[key]
        return (self.headers, "headers has been  added")

    def add_payload_dict(self,dict_payload):
        self.payload= dict_payload
        return (self.payload, "payload has been  added")

    def add_payload(self,key,value):
        if key in self.payload.keys():
            return (key,"key property already exist, try to modify")

        self.payload[key] = value
        return (self.payload[key], "payload has been  added")

    def add_params_dict(self,dict_params):
        self.payload= dict_params
        return (self.dict_params, "params has been  added")

    def add_params(self,key,value):
        if key in self.params.keys():
            return (key, "key property already exist, try to modify")

        self.params[key] = value
        return (self.params[key], "params has been  added")

    def send_request(self,method:str="GET"):
        match method:
            case "GET":
                print(f"Sending GET Request with description below:\n")
                print(f"Url:\n{self.base_url}/{self.resource_path}")
                print(f"Payload:\n{self.payload}")

                response = httpx.request("GET",
                                         url=f"{self.base_url}/{self.resource_path}",
                                         data=self.payload,
                                         timeout=10)
            case "POST":
                print(f"Sending POST Request with description below:\n")
                print(f"Url:\n{self.base_url}/{self.resource_path}")
                print(f"Payload:\n{self.payload}")

                response = httpx.request("POST",
                                         url=f"{self.base_url}/{self.resource_path}",
                                         data=self.payload,
                                         params=self.params,
                                         timeout=10)
            case "_":
                pass
        return response

    def delete_property(self,key):
        del self.payload[key]
        return (key,"key property has been deleted")

    def reset_payload(self):
        self.payload = dict()
        return (self.payload,"payload has been reset")

    def get_payload(self):
        return self.payload


# if __name__ == '__main__':
#     x = build_request('a','b')
#     print(x.get_payload())
