import sys
sys.path.append('.')

import httpx
from tools import Definition as Define

def API_GENERICFULLFILLMENT_SYNC_ENDPOINT(data ={},json={} ):
    return httpx.post(url=Define.SAMPLE,
                      params={
                          'requestid':'a3d9caa0-9ba1-452c-bd6a-83a442eda9fe'
                      },
                      headers={
                            'Content-Type': 'application/json'
                      },
                      data= data,
                      json=json)

# {'action': 'GENERICFULFILLMENTSYNC','param': [
#     {'paramname': 'TOUCHPOINT','paramvalue': 'UMB'},
#     {'paramname': 'MSISDN','paramvalue': '6287868381200'},
#     {'paramname': 'ServiceID','paramvalue': '8211022'},
#     {'paramname': 'PUSHNOTIFICATION','paramvalue': 'Y'}],'touchpoint': 'UMB'}
# curl -L -X POST 'http://10.24.139.18:15000/executerq?requestid=a3d9caa0-9ba1-452c-bd6a-83a442eda9fe' \
# -H 'Content-Type: application/json' \
# --data-raw '{
# 'action': 'GENERICFULFILLMENTSYNC',
# 'param': [
# {
# 'paramname': 'TOUCHPOINT',
# 'paramvalue': 'UMB'
# },
# {
# 'paramname': 'MSISDN',
# 'paramvalue': '6287868381200'
# },
# {
# 'paramname': 'ServiceID',
# 'paramvalue': '8211022'
# },
# {
# 'paramname': 'PUSHNOTIFICATION',
# 'paramvalue': 'Y'
# }
# ],
# 'touchpoint': 'UMB'
# }'