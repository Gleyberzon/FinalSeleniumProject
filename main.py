import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
from Locators.Home_Page_Locators import *
from Tests.test_home_page import Test_Home_Page
import datetime

Test_Home = Test_Home_Page()
Test_Home.run_all_tests()
# load_dotenv()
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get(os.getenv("HOME_PAGE_URL"))
# per = driver.find_element(*Personal.fieldset_info)
# htm = driver.find_element(*HTML_Buttons.fieldset_html_btns)
# fname = per.find_element(*Personal.input_fname)
# send = htm.find_element(*HTML_Buttons.btn_send)
# send.click()
# # fname.send_keys("Some")
# print(fname.get_attribute("validationMessage"))