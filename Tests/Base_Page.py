import os
import unittest
from abc import ABC, abstractmethod
from Util.MyFunctions import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Base_Page(unittest.TestCase, ABC):

    # Check if title is correct
    def make_test_title(self, expected_title):
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

    def make_test_selector(self, selector: Select, options, prefix):
        try:
            testName = "test_selector"
            parametres = "None"
            for option in options:
                testDescription = f"Selector: '{prefix}, try select {option}'"
                expected = f"{option} selected"
                selector.select_by_visible_text(option)
                actual = f"{selector.first_selected_option.text} selected"
                self.assertEqual(expected, actual)
                LogTest(self.path, testName, testDescription, parametres, expected, actual, True,
                        self.driver)
        except AssertionError:
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False,
                    self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)

    def make_test_input(self, text_input, text, prefix, max_len=None):
        try:
            testName = f"test_input_{prefix}"
            testDescription = "Trying to input given text"
            parametres = f"Text: {text}"
            text_input.send_keys(text)
            if max_len == None or not isinstance(max_len, int) or max_len <= 0:
                expected = f"Entered text: {text}"
            else:
                expected = f"Entered text: {text[:max_len]}"

            actual = f"Entered text: {text_input.get_attribute('value')}"
            self.assertEqual(expected, actual)
            LogTest(self.path, testName, testDescription, parametres, expected, actual, True, self.driver)
        except AssertionError:
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False, self.driver)
            self.assert_(False)
        except Exception as e:
            actual = f"Raised error: {e}"
            LogTest(self.path, testName, testDescription, parametres, expected, actual, False)
            self.assert_(False)
