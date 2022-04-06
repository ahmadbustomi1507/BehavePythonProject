@given('Ready to used MSISDN number as "123"')
def step_impl(context):
    print('data')


@when('User reset balance of the MSISDN to be "123"')
def step_impl(context):
    print('data2')

@then('The balance is successfully reset to be "123"')
def step_impl(context):
    print('data3')
