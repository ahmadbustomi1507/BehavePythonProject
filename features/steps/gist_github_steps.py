from behave import *
from selenium import webdriver
driver_path = "E:\\Project\\PythonSeleniumProject\\ChromeWebdriver\\97.0.4692.71\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
action =webdriver.ActionChains(driver)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('User successfully open browser')
def step_impl(context):
    context.driver = driver


@when('User access the website "{website}"')
def step_impl(context,website):
    context.driver.get(website)
    # context.driver.maximize_window()

@when('User Sign in  using  username "{username}" and password "{password}"')
def step_impl(context,username,password):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
        )
    finally:
        driver.find_element_by_link_text("Sign in").click()

    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'login_field')]"))
        )
    finally:
        context.driver.find_element_by_xpath("//input[contains(@id,'login_field')]").send_keys(username)
        context.driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys(password)
        context.driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()

    #<tambahin handle pop up supaya ga ngesave credentialnya>

@step('User successfully login')
def step_impl(context):
    context.driver = driver
    user_details = context.driver.find_element_by_xpath("//details[contains(@class,'details-overlay')]")
    user_details.click()
    context.driver.implicitly_wait(1)
    your_gist = context.driver.find_element_by_link_text("Your gists").is_displayed()
    user_details.click()
    assert your_gist == True, "User successfully Login"
    #user_details.click()

@when('User check the list of the gist that has been created')
def step_impl(context):
    user_details = context.driver.find_element_by_xpath("//details[contains(@class,'details-overlay')]")
    user_details.click()
    your_gist = context.driver.find_element_by_link_text("Your gists")
    your_gist.click()
    gist_list = context.driver.find_elements_by_class_name("gist-snippet")

    list_gist = []
    for gist_item in gist_list:
        item = gist_item.find_element_by_tag_name("span").text.split(' ')
        list_gist.append((item[0],item[2], item[3]))
    context.list_gist = list_gist
    context.driver.implicitly_wait(2)
    # [print(x[0]) for x in list_gist]

@when('User create the gist, with filename "{filename}", description "{description}" with content')
def step_impl(context,filename,description):
    context.driver.find_element_by_xpath("//a[contains(@data-ga-click,'go to new gist')]").click()
    Gist_description = context.driver.find_element_by_xpath("//input[contains(@name,'gist[description]')]")
    Gist_description.send_keys(description)
    Gist_filename    = context.driver.find_element_by_xpath("//input[contains(@name,'gist[contents][][name]')]")
    Gist_filename.send_keys(filename)
    Gist_content     = context.driver.find_element_by_xpath("//div[contains(@class,'CodeMirror-code')]")
    Gist_content.send_keys(context.text)
    Submit_Gist      = context.driver.find_element_by_xpath("//button[contains(text(),'Create') and contains(text(),'gist') ]")
    Submit_Gist.click()

    #go back to gist dashboard, by clicking the username
    # context.list_gist = [(username,filename,label),().....()]

    context.driver.find_element_by_link_text(context.list_gist[0][0]).click()
    context.filename = filename
    context.content = context.text

@then('New Gist has been created')
def step_impl(context):
    gist_list = context.driver.find_elements_by_class_name("gist-snippet")
    list_gist = []
    for gist_item in gist_list:
        item = gist_item.find_element_by_tag_name("span").text.split(' ')
        list_gist.append((item[0],item[2], item[3]))
    context.list_gist = list_gist

    # unpack the list, index 1
    #[(username,filename,label), () ,()]
    unzip_list_gist = list(zip(*list_gist))

    if context.filename  in unzip_list_gist[1]:
        assert True, "A new gist has been created with filename : {}".format(context.filename)

    context.driver.find_element_by_link_text(context.filename)

@when('User choose one of the gist to edit "{modified}"')
def step_impl(context,modified):
    context.filename = context.list_gist[0][1]
    context.content  = modified
    context.username = context.list_gist[0][0]

    #choose the gist
    context.driver.find_element_by_link_text(context.filename).click()
    context.driver.find_element_by_link_text("Edit").click()
    context.driver.implicitly_wait(2)

    # modify the content
    Gist_content     = context.driver.find_element_by_xpath("//div[contains(@class,'CodeMirror-code')]")
    Gist_content.send_keys(context.content)

    # submit update
    Update_Gist      = context.driver.find_element_by_xpath("//button[contains(text(),'Update') and contains(text(),'gist') ]")
    Update_Gist.click()

    context.driver.find_element_by_link_text(context.username).click()

@then('The Gist has been edited')
def step_impl(context):
    # context.driver.find_element_by_link_text(context.filename)
    simple_content=context.driver.find_element_by_xpath("//div[contains(@id,'file-{}')]".format(context.filename))
    if context.content == simple_content.text:
        assert True, "Content has been modified to \'{}\'".format(context.content)

@when('User choose one of the gist to delete')
def step_impl(context):
    context.filename = context.list_gist[0][1]
    context.username = context.list_gist[0][0]

    #choose the gist
    context.driver.find_element_by_link_text(context.filename).click()

    #debug, somehow always not interactable and they dont unique attribute for the delete Button
    # Delete_xpath      = "//button[contains(@aria-label,'Delete this Gist') and contains(text(),'Delete')]"
    form = context.driver.find_elements_by_xpath("//form[contains(@action,'/ahmadbustomi1507')]")
    for i in form:
        get_button = i.find_element_by_tag_name('button')
        if 'Delete' in get_button.text:
            get_button.click()
            break

    context.driver.implicitly_wait(1)
    alert = context.driver.switch_to.alert
    alert.accept()
    context.driver.switch_to.default_content

@then('The gist has been deleted')
def step_impl(context):
    gist_list = context.driver.find_elements_by_class_name("gist-snippet")
    list_gist = []
    for gist_item in gist_list:
        item = gist_item.find_element_by_tag_name("span").text.split(' ')
        list_gist.append((item[0],item[2], item[3]))
    context.list_gist = list_gist

    unzip_list_gist = list(zip(*list_gist))
    if context.filename not in unzip_list_gist[1]:
        assert True, "A gist has been deleted with filename : {}".format(context.filename)


@when('User sign out from the web')
def step_impl(context):
    user_details = context.driver.find_element_by_xpath("//details[contains(@class,'details-overlay')]")
    user_details.click()

    form = context.driver.find_elements_by_xpath("//form[contains(@class,'logout-form')]")
    for i in form:
        get_button = i.find_element_by_tag_name('button')
        if 'Sign out' in get_button.text:
            get_button.click()
            break
    context.driver.implicitly_wait(1)
    sign_out_confirmation = context.driver.find_element_by_xpath("//input[contains(@value,'Sign out')]")
    sign_out_confirmation.click()

@then('User successfully logout')
def step_impl(context):
    sign_up_displayed = context.driver.find_element_by_link_text("Sign up").is_displayed()

    if sign_up_displayed:
        assert True , 'User successfully logout'
    else:
        assert False, 'Logout fail'
    context.driver.quit()
