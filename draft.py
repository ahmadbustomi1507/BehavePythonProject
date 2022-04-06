from behave import *
from selenium import webdriver
driver_path = "E:\\Project\\PythonSeleniumProject\\ChromeWebdriver\\97.0.4692.71\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
action = webdriver.ActionChains(driver)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://gist.github.com/")
#driver.maximize_window()
A = driver.find_element_by_link_text("Sign in").click()
driver.implicitly_wait(5)
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@id:'login_field']"))
#     )
# finally:
driver.find_element_by_xpath("//input[contains(@id,'login_field')]").send_keys('ahmadbustomi1507@gmail.com')
driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys('1234Sial')
driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
driver.implicitly_wait(5)

user_details = driver.find_element_by_xpath("//details[contains(@class,'details-overlay')]")
user_details.click()
your_gist   = driver.find_element_by_link_text("Your gists")
your_gist.click()
gist_list   = driver.find_elements_by_class_name("gist-snippet")

list_gist = []
for gist_item in gist_list:
    item = gist_item.find_element_by_tag_name("span").text.split(' ')
    # (user, filename, label)
    list_gist.append((item[0],item[2],item[3]))


driver.find_element_by_xpath("//a[contains(@data-ga-click,'go to new gist')]").click()
# go to gist form
Gist_description = driver.find_element_by_xpath("//input[contains(@name,'gist[description]')]").send_keys('test1')
Gist_filename    = driver.find_element_by_xpath("//input[contains(@name,'gist[contents][][name]')]").send_keys('filename_test1')
driver.implicitly_wait(1)
#Gist_content     = driver.find_element_by_xpath("//textarea[contains(@name,'gist[contents][][value]')]")\
Gist_content     = driver.find_element_by_xpath("//div[contains(@class,'CodeMirror-code')]").send_keys('content')
#Gist_content.find_element_by_class_name("CodeMirror-line").click().send_keys('contain test 1')

#Button_Gist = driver.find_element_by_xpath("//div[contains(@class,'BtnGroup')]")
# List_Button_Gist = Button_Gist.find_element_by_xpath("//summary[contains(@aria-label,'Select a type of pull request')]").click()
#
# driver.implicitly_wait(2)
# Create_secret_gist = Button_Gist.find_element_by_xpath("//input[contains(@id,'gist_public_0')]").click()
# #Create_public_gist = Button_Gist.find_elements_by_xpath("//input[contains(@id,'gist_public_1')]")
#
# Submit_Gist = Button_Gist.find_element_by_xpath("//button[contains(@type,'submit')]").click()
# try:
# Summary_Button_Gist = driver.find_element_by_xpath("//summary[contains(@aria-label,'Select a type of pull request')]").click()
# Create_secret_gist = driver.find_element_by_xpath("//input[contains(@id,'gist_public_0')]")

#Create_public_gist = Button_Gist.find_elements_by_xpath("//input[contains(@id,'gist_public_1')]")
driver.implicitly_wait(2)

Submit_Gist = driver.find_element_by_xpath("//button[contains(text(),'Create') and contains(text(),'gist') ]")
Submit_Gist.click()
driver.find_element_by_link_text(list_gist[0][0])
# except:
# driver.quit()
