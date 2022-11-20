from typing import Dict,Any

class build_request(object):
    def __init__(self, domain:str, url:str):
        #ex domain:
        # www.ninjaapi.com
        self.domain = domain

        #ex url:
        # /api/v2/jne/get_location
        self.url      = url
        self.payload  = dict()

    def add_payload(self,key,value):
        if key in self.payload.keys():
            return (key,"key property already exist, try to modify")

        self.payload[key] = value
        return (self.payload[key], "payload has been  added")

    def delete_property(self,key):
        del self.payload[key]
        return (key,"key property has been deleted")

    def reset_payload(self):
        self.payload = dict()
        return (self.payload,"payload has been reset")

    def get_payload(self):
        return self.payload


if __name__ == '__main__':
    x = build_request('a','b')
    print(x.get_payload())
