import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
from Tests.test_home_page import Test_Home_Page
load_dotenv()

# print(os.path.abspath(__file__))
# driver = webdriver.Chrome()
# Test_Home = Test_Home_Page()
# Test_Home.run_all_tests()
# Test_Home.test_gender()
# Test_Home.run_all_tests()