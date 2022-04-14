from api import api_amdocs_cm as api

params= {
    'msisdn' :'6287875736063',
    'allowCancel' : 'N'
}
res = api.API_SUBSCRIBER_PROFILE_INFO_ENDPOINT(params=params)

@given('User getting the MSISDN : {MSISDN}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User getting the MSISDN : <MSISDN>')


@when('User Hit the API with the payload')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User Hit the API with the payload')


@then('User successfully hit the API with status code 200')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User successfully hit the API with status code 200')
