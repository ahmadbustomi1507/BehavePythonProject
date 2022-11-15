@given(u'my first given')
def step_impl(context):
    context.driver.get("https://www.google.com/")
    context.driver.quit()


@when(u'user do something')
def step_impl(context):
    print("my variable")


@then(u'something happen')
def step_impl(context):
    print("this is my first then")




