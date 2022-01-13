from behave import *
from selenium import webdriver
driver_path = "E:\\Project\\PythonSeleniumProject\\ChromeWebdriver\\97.0.4692.71\\chromedriver.exe"

@given('User successfully open browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=driver_path)

@when('User open the "{webaddress}" homepage')
def step_impl(context,webaddress):
    print('webaddres : {}'.format(webaddress))
    context.driver.get(webaddress)

@when('User Sign in  using  username "{username}" and password "{password}"')
def step_impl(context,username,password):
    print('locator for sign in here : {}:{}'.format(username,password))

@when('User create the gist, with filename "{filename}", description "{description}" with content')
def step_impl(context,filename,description):
    #content = getattr(context,"content",None)
    print('locator for gist creation here : {}'.format(context.text))
    #context.content.text = context.text

@when('User check the list of gists')
def step_impl(context):
    print('locator for gist list  here')

@when('User delete a gist, with filename "{filename}"')
def step_impl(context,filename):
    print('delete gist {}'.format(filename))


@when('User edit a gist, with filename "{filename}"')
def step_impl(context,filename):
    print('edit gist {}'.format(filename))
    context.driver.quit()


@then('User sucessfully logout')
def step_impl(context):
    print('logout')
