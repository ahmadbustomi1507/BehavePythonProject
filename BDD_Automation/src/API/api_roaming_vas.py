
import httpx
# from tools import Definition as Define
import asyncio

async def main(env='',payload=None):
    async with httpx.AsyncClient(timeout=10.0) as client:
        data = '<?xml version="1.0" encoding="UTF-8" standalone="no"?> <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:req="http://schemas.xl.co.id/cle/namespace/Public/Common/RequestHeader.xsd" xmlns:v1="http://schemas.xl.co.id/common/CommonResponse/V1.0" xmlns:v11="http://schemas.xl.co.id/esb/payloads/BilRoamingVAS/V1.0">  <soapenv:Header/> <soapenv:Body> <req:Header>  <req:ApplicationID>svcBilRoamingVAS</req:ApplicationID>  <req:UUID> e29b3cdc-8346-4132-b4cc-55df07fb4240</req:UUID> <req:EndSystem>JMSInstance01.XL.BIL.ROAMINGVAS.GENERAL.V1_0.REQ</req:EndSystem> <req:ComponentName>FrontEnd</req:ComponentName> </req:Header> <v11:GetSubscriberDetailsRq>' + \
                  '<v11:msisdn>' + payload + '</v11:msisdn> ' + \
                  '</v11:GetSubscriberDetailsRq> </soapenv:Body> </soapenv:Envelope>'
        # < ?xml
        # version = "1.0"
        # encoding = "UTF-8"
        # standalone = "no"? >
        # < soapenv: Envelope
        # xmlns: soapenv = "http://schemas.xmlsoap.org/soap/envelope/"
        # xmlns: req = "http://schemas.xl.co.id/cle/namespace/Public/Common/RequestHeader.xsd"
        # xmlns: v1 = "http://schemas.xl.co.id/common/CommonResponse/V1.0"
        # xmlns: v11 = "http://schemas.xl.co.id/esb/payloads/BilRoamingVAS/V1.0" >
        # < soapenv: Header / >
        # < soapenv: Body >
        # < req: Header >
        # < req: ApplicationID > svcBilRoamingVAS < / req: ApplicationID >
        # < req: UUID > 5759883502631014 < / req: UUID >
        # < req: EndSystem > JMSInstance01.XL.BIL.ROAMINGVAS.GENERAL.V1_0.REQ < / req: EndSystem >
        # < req: ComponentName > FrontEnd < / req: ComponentName >
        # < / req: Header >
        # < v11: GetSubscriberDetailsRq >
        # < v11: msisdn > 6283119304251 < / v11: msisdn >
        # < / v11: GetSubscriberDetailsRq >
        # < / soapenv: Body >
        # < / soapenv: Envelope >
        response = await client.post(url='http://roaming-vas-sit.api.devgcp.excelcom.co.id/roamingvas/v1/subscriberdetails' ,headers ={
                                    'accept'       :'*/*',
                                    'Content-Type' : 'application/xml',
                                    'ax-request-id': '233ff0c3-f0ee-4ca6-b60b-e88726e484bf',
                                    'ax-request-at': '2022-03-21T07:12:29'
                                },data=data,timeout=15.0)
        print(data)
        return response

res = asyncio.run(main(payload= '628319304251' ))
print(res)
print(res.text)
# asyncio.run(main())


