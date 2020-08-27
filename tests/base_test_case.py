import unittest

from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://the-internet.herokuapp.com/')

    def tearDown(self) -> None:
        self.driver.close()
