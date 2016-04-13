import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://10.1.22.219/AGW")


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
