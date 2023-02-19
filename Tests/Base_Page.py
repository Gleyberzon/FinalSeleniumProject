import os
import unittest
from abc import ABC, abstractmethod
from Util.MyFunctions import *
from dotenv import load_dotenv
from selenium import webdriver

class Base_Page(unittest.TestCase):


    # Check if title is correct
    def test_title(self, expected_title, driver):
        try:
            self.path = os.getenv("PATH_LOG_TESTS")
            testName = "test_title"
            testDescription = "Checking if title of page is correct"
            parametres = "None"
            expected = "Expected title: " + expected_title
            actual_title = driver.title
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
