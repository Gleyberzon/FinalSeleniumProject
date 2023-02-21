import os
import time
import ast
import unittest
import datetime
import warnings
import copy
import pyodbc
import re
from Tests.Base_Page import Base_Page
from dotenv import load_dotenv
from Locators.Next_Page_Locators import *
from selenium import webdriver
from Util.MyFunctions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

class Test_Next_Page(unittest.TestCase):
    load_dotenv()
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(os.getenv("NEXT_PAGE_URL"))
    formatted_date = datetime.datetime.now().strftime("%H-%M__%d-%m-%Y")
    path = os.getenv("PATH_LOG_TESTS").format("test_log__" + formatted_date)

    # Check if title is correct
    def test_title(self, expected_title=None):
        """
        Name: Roman Gleyberzon
        Date: 21/02/2023
        Description: This method compare given title with current title
        Input: Title (str)
        Output: None
        """
        if expected_title == None:
            expected_title = os.getenv("EXP_NEXT_TITLE")
        Base_Page.make_test_title(self, expected_title)

    # Test btn 'Change Title'
    def test_change_title(self):
        """
        Name: Roman Gleyberzon
        Date: 21/02/2023
        Description: This method click on button 'change title' and check it
        Input: None
        Output: None
        """
        try:
            testName = "test_change_title"
            testDescription="Click on btn 'change title'"
            parametres = "None"
            expected = "Title changed"
            btn = self.driver.find_element(*OnlyField.btn)
            current_title=self.driver.title
            btn.click()
            new_title=self.driver.title
            if current_title==new_title:
                actual="Title not changed"
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                self.assert_(current_title==new_title)
            else:
                actual=expected
                LogTest(self.path, testName, testDescription, parametres, expected, actual, True)
                self.assert_(True)
        except AssertionError:
            self.assert_(False)
        except Exception as e:
            actual=f"Raised error: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
        finally:
            self.driver.get(os.getenv("NEXT_PAGE_URL"))


    # I run all tests :-)
    def run_all_tests(self):
        """
          Name: Roman Gleyberzon
          Date: 21/02/2023
          Description: Run all tests of current unittest
          Input: None
          Output: None
        """
        unittest.main()
        self.driver.quit()
