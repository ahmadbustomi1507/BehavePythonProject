import copy
import sys
sys.path.append('.')

from tools import Definition as Define
from API import api_genericfullfillmentsync as api
import allure


@given('User execute the test scenario {scenario_name}')
def step_impl(context,scenario_name):
    for x in context.feature.data_environtment.keys():
        if context.feature.data_environtment[x]['scenario_name'] == scenario_name:
            scenario_id = copy.deepcopy(x)
            break

    allure.attach('''
    Scenario name: {}
    Scenario ID  : {} '''.format(scenario_name,scenario_id),
                  'nama_file.txt', allure.attachment_type.TEXT)



@given('with the MSISDN : {msisdn}')
def step_impl(context,msisdn):
    context.msisdn = msisdn
    pass

@when('User Hit the API with the payload')
def step_impl(context):
    context.res = api.API_GENERICFULLFILLMENT_SYNC_ENDPOINT(json={
                    'action': 'GENERICFULFILLMENTSYNC',
                    'param': [
                        {'paramname': 'TOUCHPOINT', 'paramvalue': 'UMB'},
                        {'paramname': 'MSISDN', 'paramvalue': context.msisdn},
                        {'paramname': 'ServiceID', 'paramvalue': '8211022'},
                        {'paramname': 'PUSHNOTIFICATION', 'paramvalue': 'Y'}],
                        'touchpoint': 'UMB'})

@then('User successfully hit the API with status code 200')
def step_impl(context):
    assert context.res.status_code == 200
    allure.attach("{}".format(context.res.text),
                  'resp.text', allure.attachment_type.TEXT)