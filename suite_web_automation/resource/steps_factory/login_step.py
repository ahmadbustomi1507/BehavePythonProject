
from behave import given,then,when
from resource.tools import credential
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from resource.pages.home_page import *

@given('user login as "{user_name}"')
def user_login(context,user_name:str):

    cre = credential.get_credential(user=user_name)
    context.driver.get(context.config.userdata['base_url'])
    try:
        element = WebDriverWait(context.driver, 1000).until(
            # EC.presence_of_element_located((By.CSS_SELECTOR, home.button_masuk))
            EC.element_to_be_clickable((By.CSS_SELECTOR, home.button_masuk))

        )
    except NoSuchElementException as e:
        print(f"Cannot find element {home.button_masuk}")
    finally:
        context.driver.find_element(By.CSS_SELECTOR,home.button_masuk).click()
        context.driver.implicitly_wait(5)

    context.driver.find_element(By.CSS_SELECTOR,home.field_masuk_username).send_keys(cre['id'])
    context.driver.find_element(By.CSS_SELECTOR,home.field_masuk_password).send_keys(cre['password'])
    context.driver.find_element(By.CSS_SELECTOR,home.button_masuk).click()
    context.driver.implicitly_wait(5)


