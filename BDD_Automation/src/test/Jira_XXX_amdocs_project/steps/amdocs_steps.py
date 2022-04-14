# from API import api_amdocs_cm as api
#
# params= {
#     'msisdn' :'6287875736063',
#     'allowCancel' : 'N'
# }
# res = api.API_SUBSCRIBER_PROFILE_INFO_ENDPOINT(params=params)
# $ behave -f allure_behave.formatter:AllureFormatter -o %result% ./features
# $ allure serve %result%

@given('User getting the MSISDN : {MSISDN}')
def step_impl(context,MSISDN):
    print('msisdn {}'.format(MSISDN))



@when('User Hit the API with the payload')
def step_impl(context):
    print('when success')


@then('User successfully hit the API with status code 200')
def step_impl(context):
    print('then success')
