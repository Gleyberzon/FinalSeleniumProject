import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
load_dotenv()

# print(os.path.abspath(__file__))
driver = webdriver.Chrome()
driver.get(os.getenv("HOME_PAGE_URL"))
input()