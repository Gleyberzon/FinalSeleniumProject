import os
import unittest
import warnings

import pyodbc
from Locators.Home_Page_Locators import *
from abc import ABC, abstractmethod
from Util.MyFunctions import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests


class Base_Page(unittest.TestCase, ABC):

    # Check if title is correct
    def make_test_title(self, expected_title):
        """
        Name: Roman Gleyberzon
        Date: 21/02/2023
        Description: This method compare given title with current title
        Input: Title (str)
        Output: None
        """
        try:
            # self.path = os.getenv("PATH_LOG_TESTS")
            testName = "test_title"
            testDescription = "Checking if title of page is correct"
            parametres = "None"
            expected = "Expected title: " + expected_title
            actual_title = self.driver.title
            actual = "Actual title: " + actual_title
            self.assertEqual(expected_title, actual_title)
            LogTest(self.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError as e:
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
            assert False
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
            assert False

    # Check if all options are selectable
    def make_test_selector(self, selector: Select, options, prefix):
        """
        Name: Roman Gleyberzon
        Date: 21/02/2023
        Description: This method tries to select all options of selector by visible text
        Input: selector, options
        Output: None
        """
        try:
            testName = "test_selector"
            parametres = "None"
            for option in options:
                testDescription = f"Selector: '{prefix}, try select {option}'"
                expected = f"{option} selected"
                selector.select_by_visible_text(option)
                actual = f"{selector.first_selected_option.text} selected"
                self.assertEqual(expected, actual)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError:
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False,
                    self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)

    # Set given text to input and check that it setted
    def make_test_input(self, text_input, text, prefix, max_len=None):
        """
        Name: Roman Gleyberzon
        Date: 21/02/2023
        Description: This method tries to set given text to input and check that it setted if max length allows
        Input: input, text, max_len(optional)
        Output: None
        """
        try:
            testName = f"test_input_{prefix}"
            testDescription = "Trying to input given text"
            parametres = f"Text: {text}"
            text_input.clear()
            text_input.send_keys(str(text))
            if max_len == None or not isinstance(max_len, int) or max_len <= 0:
                expected = f"Entered text: {text}"
            else:
                expected = f"Entered text: {text[:max_len]}"

            actual = f"Entered text: {text_input.get_attribute('value')}"
            self.assertEqual(expected, actual)
            LogTest(self.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError:
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)

    # Go to link and verify status code
    def make_test_link(self, link, linkname, title=None):
        """
        Name: Roman Gleyberzon
        Date: 21/02/2023
        Description: This method goes to url of given link and ver*ify that status code is 200
        (if given title instead of status code verify title)
        Input: link, link, linkname, title(optional)
        Output: None
        """
        try:
            testName = "test_link"
            testDescription = f"Click on link {linkname}"
            expected = "Status code 200"
            parametres = "None"
            link.send_keys(Keys.CONTROL + Keys.RETURN)

            handles = self.driver.window_handles

            self.driver.switch_to.window(handles[-1])
            if title == None:
                r = requests.get(self.driver.current_url)
                status = r.status_code
                actual = f"Status code {status}"
                self.assertEqual(expected, actual)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, True)
            else:
                expected = f"Title is: '{title}'"
                actual = f"Title is: '{self.driver.title}'"
                self.assertEqual(expected, actual)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError:
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised exception: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)
        finally:
            self.driver.close()
            self.driver.switch_to.window(handles[0])

    # Tries to send correct data (if data actually correct)
    def make_test_send_positive(self, row, conn):
        """
        Name: Roman Gleyberzon
        Date: 21/02/2023
        Description: This method get row of data from DB and tries it to send
        Input: row, connection
        Output: None
        """
        try:
            testName = "test_send_positive"
            testDescription = "In this test we take correct data from db and trying to send"
            parametres = "Given parameter: " + str(row)
            expected = f"Successfull send"
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
            html_field = self.driver.find_element(*HTML_Buttons.fieldset_html_btns)
            send_btn = html_field.find_element(*HTML_Buttons.btn_send)
            clear_btn = html_field.find_element(*HTML_Buttons.btn_clear)
            clear_btn.click()
            personId, tfname, tlname, tcity, temail, tarea, ttel, tgender = row
            if not self.is_valid_fname(tfname):
                actual = os.getenv("WRONG_ARGUMENT").format('First Name', tfname)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                self.assert_(False)
            if not self.is_valid_lname(tlname):
                actual = os.getenv("WRONG_ARGUMENT").format('Last Name', tlname)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                self.assert_(False)

            if not self.is_valid_email(temail):
                actual = os.getenv("WRONG_ARGUMENT").format('Email', temail)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                self.assert_(False)
            if not self.is_valid_city(tcity):
                actual = os.getenv("WRONG_ARGUMENT").format('City', tcity)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                self.assert_(False)
            if not self.is_valid_gender(tgender):
                actual = os.getenv("WRONG_ARGUMENT").format('Gender', tgender)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                self.assert_(False)
            if not self.is_valid_tel(ttel):
                actual = os.getenv("WRONG_ARGUMENT").format('Tel', ttel)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                self.assert_(False)
            if not self.is_valid_area(tarea):
                actual = os.getenv("WRONG_ARGUMENT").format('Email', temail)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                self.assert_(False)

            subject_cursor = conn.cursor()
            subject_cursor.execute(f"select checkbox from Subjects where id='{personId}'")
            for subject in subject_cursor:
                if not self.is_valid_subject(subject[0]):
                    actual = os.getenv("WRONG_ARGUMENT").format('Subject', subject[0])
                    LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                    self.assert_(False)
                else:
                    if subject[0] == 'Math':
                        math.click()
                    if subject[0] == 'Physics':
                        physics.click()
                    if subject[0] == 'Chemistry':
                        chemistry.click()
                    if subject[0] == 'Biology':
                        biology.click()
                    if subject[0] == 'English':
                        english.click()
                    if subject[0] == 'POP':
                        pop.click()
                    if subject[0] == 'DUD':
                        dud.click()
            fname.send_keys(tfname)
            lname.send_keys(tlname)
            email.send_keys(temail)
            tel.send_keys(ttel)
            city.select_by_visible_text(tcity)
            area.select_by_visible_text(tarea)
            if tgender == 'Male':
                mail.click()
            elif tgender == 'Female':
                femail.click()
            elif tgender == 'Other':
                other.click()
            send_btn.click()
            if fname.get_attribute('validationMessage') != '':
                actual = os.getenv("NOT_SENDED").format('First Name', tfname)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
                self.assert_(False)
            if lname.get_attribute('validationMessage') != '':
                actual = os.getenv("NOT_SENDED").format(
                    'Last Name', tlname)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
                self.assert_(False)
            if email.get_attribute('validationMessage') != '':
                actual = os.getenv("NOT_SENDED").format(
                    'Email', temail)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
                self.assert_(False)
            if tel.get_attribute('validationMessage') != '':
                actual = os.getenv("NOT_SENDED").format(
                    'Tel', ttel)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
                self.assert_(False)
            LogTest(self.path, testName, testDescription, parametres, expected, expected, True)
            self.assert_(True)
        except AssertionError as e:
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)

    # Tties to send incorrect data
    def make_test_send_negative(self, row, conn):
        """
        Name: Roman Gleyberzon
        Date: 21/02/2023
        Description: This method get row of data from DB and tries it to send
        Input: row, connection
        Output: None
        """
        try:
            parametres = None
            actual = ""
            testName = "test_send_negative"
            testDescription = "In this test we take incorrect data from db and trying to send"
            expected = f"Unsuccessfull send"
            # Init fields
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
            html_field = self.driver.find_element(*HTML_Buttons.fieldset_html_btns)
            send_btn = html_field.find_element(*HTML_Buttons.btn_send)
            clear_btn = html_field.find_element(*HTML_Buttons.btn_clear)
            # -- End Init fields --
            clear_btn.click()
            personId, tfname, tlname, tcity, temail, tarea, ttel, tgender = row
            dataValid = True
            correct_params = []
            incorrect_params = []
            # Fname
            if not self.is_valid_fname(tfname):
                incorrect_params.append(f"First Name: {tfname}")
                dataValid = False
            else:
                correct_params.append(f"First Name: {tfname}")
            # Lname
            if not self.is_valid_lname(tlname):
                incorrect_params.append(f"Last Name: {tlname}")
                dataValid = False
            else:
                correct_params.append(f"Last Name: {tfname}")
            # Email
            if not self.is_valid_email(temail):
                incorrect_params.append(f"Email: {temail}")
                dataValid = False
            else:
                correct_params.append(f"Email: {temail}")
            # City
            if not self.is_valid_city(tcity):
                warnings.warn(os.getenv("WILL_REPLACED").format("City", tcity, os.getenv("CORRECT_DEFOULT_CITY")))
                tcity = os.getenv("CORRECT_DEFOULT_CITY")
                correct_params.append(f"City: {tcity}")
            else:
                correct_params.append(f"City: {tcity}")
            # Gender
            if not self.is_valid_gender(tgender):
                warnings.warn(os.getenv("WILL_REPLACED").format("Gender", tgender, 'Other'))
                tgender = 'Other'
                correct_params.append(f"Gender: {tgender}")
            else:
                correct_params.append(f"Gender: {tgender}")
            if tgender == 'Male':
                mail.click()
            elif tgender == 'Female':
                femail.click()
            elif tgender == 'Other':
                other.click()
            # Tel
            if not self.is_valid_tel(ttel):
                incorrect_params.append(f"Tel: {ttel}")
                dataValid = False
            else:
                correct_params.append(f"Tel: {ttel}")
            # Area
            if not self.is_valid_area(tgender):
                warnings.warn(os.getenv("WILL_REPLACED").format("Area", tarea, os.getenv("CORRECT_DEFOUL_AREA")))
                tarea = os.getenv("CORRECT_DEFOUL_AREA")
                correct_params.append(f"Area: {tarea}")
            else:
                correct_params.append(f"Area: {tarea}")
            # Subjects
            subject_cursor = conn.cursor()
            subject_cursor.execute(os.getenv("QUERY_SUBJECTS").format(personId))
            subjects = []
            for subject in subject_cursor:
                if not self.is_valid_subject(subject[0]):
                    warnings.warn(os.getenv("WILL_NOT_CHECKED").format("Subject", subject[0]))
                else:
                    if subject[0] == 'Math':
                        math.click()
                        subjects.append('Math')
                    if subject[0] == 'Physics':
                        physics.click()
                        subjects.append('Physics')
                    if subject[0] == 'Chemistry':
                        chemistry.click()
                        subjects.append('Chemistry')
                    if subject[0] == 'Biology':
                        biology.click()
                        subjects.append('Biology')
                    if subject[0] == 'English':
                        english.click()
                        subjects.append('English')
                    if subject[0] == 'POP':
                        pop.click()
                        subjects.append('POP')
                    if subject[0] == 'DUD':
                        dud.click()
                        subjects.append('DUD')
            parametres = "\nCorrect parametres: " + ", ".join(correct_params)
            parametres += "\nSubjects: " + ", ".join(subject)
            parametres += "\nIncorrect parametres: " + ", ".join(incorrect_params)

            if dataValid:
                actual = os.getenv("NOT_SUIT")
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
                self.assert_(False)

            # Send keys
            fname.send_keys(tfname)
            lname.send_keys(tlname)
            email.send_keys(temail)
            tel.send_keys(ttel)
            city.select_by_visible_text(tcity)
            area.select_by_visible_text(tarea)
            send_btn.click()
            # Result

            # Check Fname
            if not self.is_valid_fname(tfname) and fname.get_attribute('validationMessage') == '':
                actual = os.getenv("IDENTIFIED_AS_VALID").format('First Name', tfname)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
                self.assert_(False)
            elif fname.get_attribute('validationMessage') != '':
                LogTest(self.path, testName, testDescription, parametres, expected, expected, True)
                self.assert_(True)
                return
            # Check Lname
            if not self.is_valid_lname(tlname) and lname.get_attribute('validationMessage') == '':
                actual = os.getenv("IDENTIFIED_AS_VALID").format('Last Name', tlname)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
                self.assert_(False)
            elif lname.get_attribute('validationMessage') != '':
                LogTest(self.path, testName, testDescription, parametres, expected, expected, True)
                self.assert_(True)
                return
            # Check Email
            if not self.is_valid_email(temail) and email.get_attribute('validationMessage') == '':
                actual = os.getenv("IDENTIFIED_AS_VALID").format('Email', temail)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
                self.assert_(False)
            elif email.get_attribute('validationMessage') != '':
                LogTest(self.path, testName, testDescription, parametres, expected, expected, True)
                self.assert_(True)
                return
            # Check Tel
            if not self.is_valid_tel(ttel) and tel.get_attribute('validationMessage') == '':
                actual = os.getenv("IDENTIFIED_AS_VALID").format('Tel', ttel)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
                self.assert_(False)
            LogTest(self.path, testName, testDescription, parametres, expected, expected, True)


        except AssertionError:
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)


    # Set text to prompt
    def make_test_set_test(self, text):
        """
          Name: Roman Gleyberzon
          Date: 21/02/2023
          Description: This method check setting text to prompt
          Input: None
          Output: None
        """
        try:
            testName = "test_set_test"
            testDescription = "Try to set text to prompt"
            field = self.driver.find_element(*JS_Area.fieldset_js_btns)
            table = field.find_element(*JS_Area.text_field)
            btn = field.find_element(*JS_Area.btn_set_text)
            btn.click()
            alert = self.driver.switch_to.alert
            alert.send_keys(text)
            alert.accept()
            parametres = f"Text: {text}"
            expected = f"Setted text: {text}"
            ls = list(table.text)
            for i in range(len(ls)):
                if ls[i] == '\n':
                    ls[i] = '\\n'
                if ls[i] == '\t':
                    ls[i] = '\\t'
                if ls[i] == '\b':
                    ls[i] = '\\b'
            actual = f"Setted text: {''.join(ls)}"
            self.assertEqual(expected,actual)
            LogTest(self.path, testName, testDescription, parametres, expected, actual, True)
        except AssertionError as e:
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
