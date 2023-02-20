import os
import time
import ast
import unittest
import datetime
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
from selenium.webdriver.support.ui import Select


class Test_Home_Page(Base_Page, unittest.TestCase):
    load_dotenv()
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(os.getenv("HOME_PAGE_URL"))
    formatted_date = datetime.datetime.now().strftime("%H-%M__%d-%m-%Y")
    path = os.getenv("PATH_LOG_TESTS").format("test_log__" + formatted_date)

    # Check if title is correct
    def test_title(self, expected_title=None, dr=None):
        if expected_title == None:
            expected_title = os.getenv("EXP_HOME_TITLE")
        if dr == None:
            dr = Test_Home_Page.driver
        Base_Page.make_test_title(self, expected_title)

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
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)

    def test_checkboxes(self):
        try:
            testName = "test_checkboxes"
            parametres = "None"
            fieldset_info = self.driver.find_element(*Personal.fieldset_info)
            lsCheckers = {}
            lsCheckers["biology"] = fieldset_info.find_element(*Personal.checkbox_biology)
            lsCheckers["chemistry"] = fieldset_info.find_element(*Personal.checkbox_chemistry)
            lsCheckers["math"] = fieldset_info.find_element(*Personal.checkbox_math)
            lsCheckers["english"] = fieldset_info.find_element(*Personal.checkbox_english)
            lsCheckers["physics"] = fieldset_info.find_element(*Personal.checkbox_phisics)
            lsCheckers["dud"] = fieldset_info.find_element(*Personal.checkbox_dud)
            lsCheckers["pop"] = fieldset_info.find_element(*Personal.checkbox_pop)
            for key, el in lsCheckers.items():
                testDescription = f"First click on {key}"
                expected = f"{key} checked"
                el.click()
                actual = f"{key} {'checked' if el.is_selected() else 'not checked'}"
                self.assertEqual(expected, actual)
                LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, True)
                testDescription = f"Second click on {key}"
                expected = f"{key} not checked"
                el.click()
                actual = f"{key} {'checked' if el.is_selected() else 'not checked'}"
                LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError:
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)

    def test_selector_city(self):
        options = ast.literal_eval(os.getenv("CITiES"))
        field = self.driver.find_element(*Personal.fieldset_info)
        selector = Select(field.find_element(*Personal.selector_city))
        prefix = "City"
        Base_Page.make_test_selector(self, selector, options, prefix)

    def test_selector_area_code(self):
        options = ast.literal_eval(os.getenv("AREA_CODES"))
        field = self.driver.find_element(*Personal.fieldset_info)
        selector = Select(field.find_element(*Personal.selector_area_code))
        prefix = "Area code"
        Base_Page.make_test_selector(self, selector, options, prefix)

    def test_input_fname(self):
        field = self.driver.find_element(*Personal.fieldset_info)
        input = field.find_element(*Personal.input_fname)
        text = os.getenv("TEST_FNAME")
        prefix = "First Name"
        Base_Page.make_test_input(self, input, text, prefix, int(os.getenv("MAX_LEN")))

    def test_input_lname(self):
        field = self.driver.find_element(*Personal.fieldset_info)
        input = field.find_element(*Personal.input_lname)
        text = os.getenv("TEST_LNAME")
        prefix = "Last Name"
        Base_Page.make_test_input(self, input, text, prefix, int(os.getenv("MAX_LEN")))

    def test_input_email(self):
        field = self.driver.find_element(*Personal.fieldset_info)
        input = field.find_element(*Personal.input_email)
        text = os.getenv("TEST_EMAIL")
        prefix = "Email"
        Base_Page.make_test_input(self, input, text, prefix)

    def test_input_tel(self):
        field = self.driver.find_element(*Personal.fieldset_info)
        input = field.find_element(*Personal.input_tel)
        text = os.getenv("TEST_TEL")
        prefix = "Tel"
        Base_Page.make_test_input(self, input, text, prefix)

    def test_clear(self):
        try:
            testName = "test_clear"
            testDescription = "Test of button 'Clear"
            parametres = "None"
            expected = f"All inputs epmty. Selector city have value '{os.getenv('CORRECT_DEFOULT_CITY')}'. Selector Area Code have value '{os.getenv('CORRECT_DEFOUL_AREA')}'. All radio and checkers unselected."
            field = self.driver.find_element(*Personal.fieldset_info)
            fname = field.find_element(*Personal.input_fname)
            lname = field.find_element(*Personal.input_lname)
            email = field.find_element(*Personal.input_email)
            tel = field.find_element(*Personal.input_tel)
            femail = field.find_element(*Personal.radio_female)
            mail = field.find_element(*Personal.radio_mail)
            other = field.find_element(*Personal.radio_other)
            math = field.find_element(*Personal.checkbox_math)
            physics = field.find_element(*Personal.checkbox_phisics)
            biology = field.find_element(*Personal.checkbox_math)
            chemistry = field.find_element(*Personal.checkbox_chemistry)
            english = field.find_element(*Personal.checkbox_english)
            pop = field.find_element(*Personal.checkbox_pop)
            dud = field.find_element(*Personal.checkbox_dud)

        except AssertionError:
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)

    def run_all_tests(self):
        unittest.main()
