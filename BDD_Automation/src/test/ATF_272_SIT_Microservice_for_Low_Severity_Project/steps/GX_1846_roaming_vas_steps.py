from API import api_roaming_vas as api
# from tools import Definition
# import asyncio
#
# res = asyncio.run( api.main(payload= '628319304251' ))
# print(res.text)

@step('get the test scenario name : {scenario_name}')
def step_impl(context,scenario_name):
    print('\tscenario_name : {}\n\n'.format(scenario_name))

@given(u'User getting the MSISDN Target : {msisdn}')
def step_impl(context,msisdn):
    print('\ttest 2\n\n')

@step('User getting the MSISDN Target : {msisdn} with type : {type}')
def step_impl(context,msisdn,type):
    # rows = context.table.rows
    # print('data_releng {}'.format(context.data_releng))
    context.msisdn = msisdn
    print('\tdata_environtment {}\n\n'.format(context.feature.data_environtment))
    print('\tfeature table {}\n\n'.format(context.table))


@when('User Hit the API with the payload')
def step_impl(context):
    print('\tini when\n\n')

@then('User successfully hit the API with status code 200')
def step_impl(context):
    print('ini then\n\n')
