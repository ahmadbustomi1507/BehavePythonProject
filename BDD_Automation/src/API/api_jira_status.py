from tools import Definition as Define
import httpx

'''
Berikut API untuk update status di Jira dengan sample tiket HYG-5578 :



curl --location --request POST 'https://collabs.xl.co.id/rest/api/2/issue/HYG-5578/transitions' \
--header 'Authorization: Basic xxxx' \
--header 'Content-Type: application/json' \
--data-raw '{"transition": {"id": "11"}}'

Untuk mengetahui transisition id, silakan bisa get transition dulu dengan api berikut :

curl --location --request GET 'https://collabs.xl.co.id/rest/api/2/issue/HYG-5578/transitions' \
--header 'Authorization: Basic xxx' \


'''
import httpx
import base64

async def main(jira_id ='',data ={},json={},Username='' , Password = ''):
    async with httpx.AsyncClient(timeout=10.0) as client:
        enc = base64.b64encode(bytes('{}:{}'.format(username,password),'utf-8'))
        response = await client.post(url=Define.API_JIRA_STATUS_ENDPOINT + jira_id + '/transitions',
                      params=None,
                      headers={
                            'Content-Type': 'application/json',
                            'Authorization': 'Basic ' + enc.decode('utf-8')
                      },
                      data= data,
                      json=json,timeout=15.0)
        return response
