import os
import time
import unittest
from Tests.Base_Page import Base_Page
from dotenv import load_dotenv
from Locators.Home_Page_Locators import *
from selenium import webdriver
from Util.MyFunctions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Test_Home_Page(Base_Page, unittest.TestCase):

    load_dotenv()
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(os.getenv("HOME_PAGE_URL"))
    path = os.getenv("PATH_LOG_TESTS")
    def setUp(self):
        pass

    def test_gender(self):
        try:
            testName = "test_gender"
            parametres = "None"
            fieldset_info = self.driver.find_element(*Personal.fieldset_info)
            radio_mail = fieldset_info.find_element(*Personal.radio_mail)
            radio_femail = fieldset_info.find_element(*Personal.radio_female)
            radio_other = fieldset_info.find_element(*Personal.radio_other)

            def gender_status():
                mail = 'selected' if radio_mail.is_selected() else 'not selected'
                femail = 'selected' if radio_femail.is_selected() else 'not selected'
                other = 'selected' if radio_other.is_selected() else 'not selected'
                return mail, femail, other

            testDescription = "Checking of choosing Male gender"
            # Check Male
            radio_mail.click()
            mail, femail, other = gender_status()
            expected = "Gender 'Male' selected, Gender 'Female' not selected, Gender 'Other' not selected."
            actual = f"Gender 'Male' {mail}, Gender 'Female' {femail}, Gender 'Other' {other}."
            self.assertEqual(expected, actual)
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, True)
            # Check female
            testDescription = "Checking of choosing Femail gender"
            expected = "Gender 'Male' not selected, Gender 'Female' selected, Gender 'Other' not selected."
            radio_femail.click()
            mail, femail, other = gender_status()
            actual = f"Gender 'Male' {mail}, Gender 'Female' {femail}, Gender 'Other' {other}."
            self.assertEqual(expected, actual)
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, True)

            # Check other
            testDescription = "Checking of choosing Other gender"
            expected = "Gender 'Male' not selected, Gender 'Female' not selected, Gender 'Other' selected."
            radio_other.click()
            mail, femail, other = gender_status()
            actual = f"Gender 'Male' {mail}, Gender 'Female' {femail}, Gender 'Other' {other}."
            self.assertEqual(expected, actual)
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError:
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)

    # Check if title is correct

    def test_title(self, expected_title=None, dr=None):
        if expected_title == None:
            expected_title = os.getenv("EXP_HOME_TITLE")
        if dr==None:
            dr=Test_Home_Page.driver
        Base_Page.test_title(self, expected_title, dr)

    def run_all_tests(self):
        unittest.main()
