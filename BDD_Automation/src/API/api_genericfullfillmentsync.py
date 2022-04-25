import sys
sys.path.append('.')

import httpx
from tools import Definition as Define

async def main(data ={},json={}):
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(url=Define.SAMPLE,
                      params={
                          'requestid':'a3d9caa0-9ba1-452c-bd6a-83a442eda9fe'
                      },
                      headers={
                            'Content-Type': 'application/json'
                      },
                      data= data,
                      json=json,timeout=15.0)
        return response

def API_GENERICFULLFILLMENT_SYNC_ENDPOINT(data ={},json={} ,proxy=None, requestid='a3d9caa0-9ba1-452c-bd6a-83a442eda9fe'):
    with httpx.Client(proxies=proxy) as client:
        request = httpx.Request("POST",url=Define.SAMPLE,
                      params={
                          'requestid':requestid
                      },
                      headers={
                            'Content-Type': 'application/json',
                            'accept':'*/*'
                       },
                      data= data,
                      json=json)
        response = client.send(request)

        return (request,response)
