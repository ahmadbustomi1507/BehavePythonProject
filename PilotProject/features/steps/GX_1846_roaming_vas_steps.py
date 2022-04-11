from API import roaming_vas as api

@step('User getting the MSISDN Target : {msisdn} with type : {type}')
def step_impl(context,msisdn,type):
    print('ini given {} {}'.format(type,msisdn))
    context.msisdn = msisdn

@when('User Hit the API with the payload')
def step_impl(context):
    print('ini when')

@then('User successfully hit the API with status code 200')
def step_impl(context):
    print('ini then')
