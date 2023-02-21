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
            city = Select(field.find_element(*Personal.selector_city))
            area = Select(field.find_element(*Personal.selector_area_code))
            fname.clear()
            lname.clear()
            email.clear()
            tel.clear()
            tfname,tlname,temail,ttel,tarea,tcity = ast.literal_eval(os.getenv("CLEAR_INPUT"))
            fname.send_keys(tfname)
            lname.send_keys(tlname)
            email.send_keys(temail)
            tel.send_keys(ttel)
            femail.click()
            area.select_by_visible_text(tarea)
            city.select_by_visible_text(tcity)
            math.click()
            physics.click()
            biology.click()
            chemistry.click()
            english.click()
            pop.click()
            dud.click()
            htmlField = self.driver.find_element(*HTML_Buttons.fieldset_html_btns)
            clearBtn=htmlField.find_element(*HTML_Buttons.btn_clear)
            clearBtn.click()
            actual = f"Field fname have text: {fname.get_attribute('value')}"
            self.assert_(fname.get_attribute('value')=="")
            actual = f"Field lname have text: {lname.get_attribute('value')}"
            self.assert_(lname.get_attribute('value') == "")
            actual = f"Field email have text: {email.get_attribute('value')}"
            self.assert_(email.get_attribute('value') == "")
            actual = f"Field tel have text: {tel.get_attribute('value')}"
            self.assert_(tel.get_attribute('value') == "")
            actual = f"Field mail: {'selected' if mail.is_selected() else 'not selected'}"
            self.assert_(not mail.is_selected())
            actual = f"Field femail: {'selected' if femail.is_selected() else 'not selected'}"
            self.assert_(not femail.is_selected())
            actual = f"Field other: {'selected' if other.is_selected() else 'not selected'}"
            self.assert_(not other.is_selected())
            actual = f"Field math: {'selected' if math.is_selected() else 'not selected'}"
            self.assert_(not math.is_selected())
            actual = f"Field biology: {'selected' if biology.is_selected() else 'not selected'}"
            self.assert_(not biology.is_selected())
            actual = f"Field chemistry: {'selected' if chemistry.is_selected() else 'not selected'}"
            self.assert_(not chemistry.is_selected())
            actual = f"Field physics: {'selected' if physics.is_selected() else 'not selected'}"
            self.assert_(not physics.is_selected())
            actual = f"Field english: {'selected' if english.is_selected() else 'not selected'}"
            self.assert_(not english.is_selected())
            actual = f"Field POP: {'selected' if pop.is_selected() else 'not selected'}"
            self.assert_(not pop.is_selected())
            actual = f"Field DUD: {'selected' if mail.is_selected() else 'not selected'}"
            self.assert_(not dud.is_selected())
            actual = f"Field city: {city.first_selected_option.text}"
            self.assert_(city.first_selected_option.text == os.getenv("CORRECT_DEFOULT_CITY"))
            actual = f"Field area code: {area.first_selected_option.text}"
            self.assert_(area.first_selected_option.text == os.getenv("CORRECT_DEFOUL_AREA"))
            actual = expected
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError:
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)

    def test_send_positive(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-NRHU0LQ\\SQLEXPRESS;'
                              'Database=correct_db_persons;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from persons")
        rows = []
        for row in cursor:
            rows.append(row)
        assertStatus = True
        for row in rows:
            try:
                Base_Page.make_test_send_positive(self,row, conn)
            except:
                assertStatus = False
        if not assertStatus:
            raise AssertionError
    def test_send_negative(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-NRHU0LQ\\SQLEXPRESS;'
                              'Database=incorrect_db_persones;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from persons")
        rows = []
        assertStatus = True
        for row in cursor:
            rows.append(row)
        for row in rows:
            try:
                Base_Page.make_test_send_negative(self,row, conn)
            except:
                assertStatus=False
        if not assertStatus:
            raise AssertionError



    def test_set_test(self):
        try:
            testName = "test_set_test"
            testDescription = "Try to set text to prompt"
            text = os.getenv("TEXT")
            field = self.driver.find_element(*JS_Area.fieldset_js_btns)
            table = field.find_element(*JS_Area.text_field)
            btn = field.find_element(*JS_Area.btn_set_text)
            btn.click()
            alert = self.driver.switch_to.alert
            alert.send_keys(text)
            alert.accept()
            parametres = f"Text: {text}"
            expected = f"Setted text: {text}"
            actual = f"Setted text: {table.text}"
            self.assertEqual(expected,actual)
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError as e:
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)

    def test_start_loading(self):
        try:
            testName = "test_start_loading"
            testDescription = "Click on start loading"
            expected = "Printed text 'Finish'"
            parametres = "None"
            field = self.driver.find_element(*JS_Area.fieldset_js_btns)
            status = field.find_element(*JS_Area.text_status_loading)
            btn = field.find_element(*JS_Area.btn_start_loading)
            try:
                btn.click()
                WebDriverWait(self.driver, 10).until(ec.text_to_be_present_in_element(JS_Area.text_status_loading,'Finish'))
            except:
                actual = "Not printed 'Finish'"
                raise AssertionError
            actual = expected
            self.assertEqual(expected,actual)
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError as e:
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(Test_Home_Page.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)

    def test_link_windy(self):
        field = self.driver.find_element(*Links.fieldset_links)
        link = field.find_element(*Links.link_windy)
        Base_Page.make_test_link(self,link,"Windy")

    def test_link_youtube(self):
        field = self.driver.find_element(*Links.fieldset_links)
        link = field.find_element(*Links.link_youtube)
        Base_Page.make_test_link(self,link,"YouTube")

    def test_link_tera_santa(self):
        field = self.driver.find_element(*Links.fieldset_links)
        link = field.find_element(*Links.link_tera_santa)
        Base_Page.make_test_link(self,link,"Tera Santa")

    def test_link_java_book(self):
        field = self.driver.find_element(*Links.fieldset_links)
        link = field.find_element(*Links.link_java_book)
        Base_Page.make_test_link(self,link,"Java Book")

    def test_link_next_page(self):
        field = self.driver.find_element(*Links.fieldset_links)
        link = field.find_element(*Links.link_next_page)
        Base_Page.make_test_link(self,link,"Next Page", "Next Page")


    def is_valid_fname(self, name):
        if len(name)>int(os.getenv("MAX_LEN") or len(name)<2):
            return False
        return not not re.fullmatch(r"[A-z]*",name)

    def is_valid_lname(self, name):
        if len(name)>int(os.getenv("MAX_LEN") or len(name)<2):
            return False
        return not not re.fullmatch(r"[A-z]*",name)

    def is_valid_email(self, email):
        return not not re.fullmatch(r"^(?:(?!.*?[.]{2})[a-zA-Z0-9](?:[a-zA-Z0-9.+!%-]{1,64}|)|\"[a-zA-Z0-9.+!% -]{1,64}\")@[a-zA-Z0-9][a-zA-Z0-9.-]+(.[a-z]{2,}|.[0-9]{1,})",email)

    def is_valid_tel(self, tel):
        if len(tel)!=7:
            return False
        return re.fullmatch(r"[0-9]*", tel)

    def is_valid_city(self, city):
        return city in ast.literal_eval(os.getenv("CITiES"))

    def is_valid_area(self, area):
        return area in ast.literal_eval(os.getenv("AREA_CODES"))

    def is_valid_subject(self, subject):
        return subject in ast.literal_eval(os.getenv("SUBJECTS"))

    def is_valid_gender(self, gender):
        return gender in ast.literal_eval(os.getenv("GENDERS"))

    def run_all_tests(self):
        unittest.main()


