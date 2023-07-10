from selenium.webdriver.common.by import By
import pdb

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *

@given(u'user successfully access login page of saucedemo')
def step_impl(context):
    context.driver.get( context.config.userdata['base_url'])
    context.driver.implicitly_wait(10)

@when('user fill in username "{username}" and password "{password}"')
def step_impl(context,username,password):
    ## cssLogin = ".login-box input#user-name"
    context.driver.find_element(By.CSS_SELECTOR,".login-box input#user-name").send_keys(username)
    context.driver.implicitly_wait(5)

    ## cssPassword = ".login-box input#password"
    context.driver.find_element(By.CSS_SELECTOR, ".login-box input#password").send_keys(password)
    context.driver.implicitly_wait(5)

    #click login button
    ## cssButton = .login-box input#login-button
    context.driver.find_element(By.CSS_SELECTOR, ".login-box input#login-button").click()

@then(u'user successfully redirect to homepage')
def step_impl(context):
    # assert the current url
    context.driver.implicitly_wait(5)
    print(f"current page {context.driver.current_url}")
    assert context.driver.current_url == "https://www.saucedemo.com/inventory.html"

    # assert the list of items exist
    # cssInventoryList =div#inventory_container div.inventory_list
    assert True == context.driver.find_element(By.CSS_SELECTOR,"div#inventory_container div.inventory_list")\
        .is_displayed()

@then(u'user will get correct image in the items')
@then(u'user will get wrong image in the items')
def step_impl(context):
    # get all the name of the image
    list_image_text = context.driver.execute_script('''
            var inventoryItem = document.getElementsByClassName("inventory_item");
            var arrayText = [];
            inventoryItem.forEach((x)=>{
                    imgText = x.querySelector("img").getAttribute("src")
                    arrayText.push(imgText)                  
                }
            );
            console.log(arrayText);
            return arrayText;
     ''')
    assert "/static/media/sl-404.168b1cce.jpg" not in list_image_text, "the wrong image is found the list items"

@then(u'user will get message error as "{message}"')
def step_impl(context,message ):
    "Epic sadface: Sorry, this user has been locked out."
    error_box = context.driver.find_element(By.CSS_SELECTOR,"div.error-message-container")
    assert error_box.text == "Epic sadface: Sorry, this user has been locked out."

@then(u'user will redirect to homepage after timeout "{time}" sec')
def step_impl(context,time):
    try:
       WebDriverWait(context.driver, time).until(expected_conditions.presence_of_all_elements_located(
            (By.CSS_SELECTOR,"div#inventory_container div.inventory_list div.inventory.item")
        ))
    except TimeoutException as E:
        assert False,f"Web page didnt show up even after waiting {time} sec"
    finally:
        assert True == context.driver.find_element(By.CSS_SELECTOR,"div#inventory_container div.inventory_list")\
            .is_displayed()
