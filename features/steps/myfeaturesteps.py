from behave import *
from selenium import webdriver
driver_path = "E:\\Project\\PythonSeleniumProject\\ChromeWebdriver\\97.0.4692.71\\chromedriver.exe"

# @given("Launch chrome")
# def method1(context):
#     context.driver = webdriver.Chrome(executable_path=driver_path)
#
# @when("Open Orange")
# def method2(context):
#     context.driver.get("https://opensource-demo.orangehrmlive.com/")
#
# @then("Verify")
# def method3(context):
#     status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
#     assert status is True
#
# @then("Close Browser")
# def method4(context):
#     context.driver.close()

@given('i launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=driver_path)


@when('i Open Orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()

@then('user must successfully login to the dashboard page')
def step_impl(context):
    try:
        text_dashboard =context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text_
    except:
        context.driver.close()
        assert False,"Test fail, Dashboard not found"

    if text_dashboard =="Dashboard":
        assert True, "Test passed"
