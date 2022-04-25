
import sys
sys.path.append('.')

import allure
import asyncio
import uuid

from tools import Utility as Ut
from tools import Definition as Define

from behave.api.async_step import async_run_until_complete
from API import api_genericfullfillmentsync as api

@given('User execute the test scenario {scenario_id} {scenario_name}')
@async_run_until_complete
async def step_impl(context,scenario_id,scenario_name):
    await asyncio.sleep(10)
    allure.attach('''Scenario name: {}\nScenario ID  :{} '''.format(scenario_name,scenario_id),
                  'nama_file.txt', allure.attachment_type.TEXT)

@given('with the MSISDN : {msisdn}')
def step_impl(context,msisdn):
    context.msisdn = msisdn
    pass

@when('User Hit the API with the payload')
@async_run_until_complete
async def step_impl(context):
    await asyncio.sleep(10)
    data_payload = {'action': 'GENERICFULFILLMENTSYNC',
                    'param': [
                        {'paramname': 'TOUCHPOINT', 'paramvalue': 'UMB'},
                        {'paramname': 'MSISDN', 'paramvalue': context.msisdn},
                        {'paramname': 'ServiceID', 'paramvalue': '8211022'},
                        {'paramname': 'PUSHNOTIFICATION', 'paramvalue': 'Y'}],
                        'touchpoint': 'UMB'}

    context.uuid4 = str(uuid.uuid4())
    context.req, context.res     = api.API_GENERICFULLFILLMENT_SYNC_ENDPOINT(json=data_payload,requestid=context.uuid4)

    # (DONE) tambahin  request
    allure.attach('''Request Header\t: {}\nRequest Content header\t: {}\n'''.format(
        context.req.headers,
        context.res.content.decode('ascii'),
    ),'request.text', allure.attachment_type.TEXT)

@then('User successfully hit the API with status code 200')
@async_run_until_complete
async def step_impl(context):
    await asyncio.sleep(10)
    allure.attach('''status code : {}\nheader      : {}\ntext        : {}\n'''.format(
        context.res.status_code,
        context.res.headers,
        context.res.text,
    ),'response.text', allure.attachment_type.TEXT)
    assert context.res.status_code == 200, "status codenya bukan 200 ngab, tapi {}".format(context.res.status_code)
    # (DONE) tambahin  response

    query = '''
        SELECT msisdn, sys_creation_date, soccd, serviceid, completionstatus, CD_MAIN_ID, esbuuid, policyname, operationname, expirationdate, benefittype, exceptioncode, exceptiondescription
        FROM SOARTT_MISCKPI
        WHERE msisdn = '6287868381200'
        AND esbuuid = '{}'
        ORDER BY sys_creation_date DESC'''.format(context.uuid4)

    # refer to this
    # https://stackoverflow.com/questions/56119490/cx-oracle-error-dpi-1047-cannot-locate-a-64-bit-oracle-client-library
    records = Ut.query_oracle(config=Define.SOAR_TRCKTRACE_DB_ORACLE , query = query)
    record  = [ rec for rec in records ]

    allure.attach('''records with esuuid: \n{}'''.format(
            record
        ), 'records.text', allure.attachment_type.TEXT)


    query = '''
        SELECT msisdn, sys_creation_date, soccd, serviceid, completionstatus, CD_MAIN_ID, esbuuid, policyname, operationname, expirationdate, benefittype, exceptioncode, exceptiondescription
        FROM SOARTT_MISCKPI
        WHERE msisdn = '6287868381200'
        ORDER BY sys_creation_date DESC'''

    # refer to this
    # https://stackoverflow.com/questions/56119490/cx-oracle-error-dpi-1047-cannot-locate-a-64-bit-oracle-client-library
    records = Ut.query_oracle(config=Define.SOAR_TRCKTRACE_DB_ORACLE , query = query)
    record  = [ rec for rec in records ]

    allure.attach('''records : \n{}'''.format(
            record
        ), 'records.text', allure.attachment_type.TEXT)