'''
Q:
Create script (any language programming) to get output as below:
^
***
^^^^
*******
^^^^^^^^^^^
1 3 4 7 11
'''
index     = 0 1 2 3  4  5
jumlahnya = 1 3 4 7 11 18
bentuk    = ^ * ^ * ^  *

from copy import *
x = 0
y = 0
for i in  range(0,6):
   print ('*' * i)
   x = copy(i)
index 1 3 5 7 '^'
index 0 2 4 6 '*'

# Create selenium script to launch 'google.com' and search 'Verint' and validate the result is returned as expected.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "E:\\Project\\PythonSeleniumProject\\ChromeWebdriver\\97.0.4692.71\\chromedriver.exe"
driver  = webdriver.Chrome(driver_path)

url         = "https:\\www.gooogle.com"
search_loc = "//input[contains(@class,'gLFyf')]"
keyword_search = 'Verint'

driver.get(url)
driver.find_element(By.XPATH,search_loc).click().send_keys(keyword_search).send_keys(Return)
<send enter>
<send explicit time>

text_verint = driver.find_elements(By.CLASS_NAME,"v7W49e")

assert "Verint" in text_verint