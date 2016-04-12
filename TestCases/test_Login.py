import unittest

from ddt import ddt,data,unpack
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from BaseTestCases.BaseTestCase import BaseTestCase
from DataSource.read_excel import read_excel

@ddt
class LoginTest(BaseTestCase):


    @data(*read_excel.get_data_from_excel('C:/Users/efarrag/PycharmProjects/ACE_Automation001/Data/login_data.xlsx','login'))
    @unpack
    def test_login_with_valid_credentials(self,Username,Password,LoginName):
        LoginPage.login(self,Username,Password)
        self.assertEqual(LoginName,HomePage.get_login_name(self))
        print(HomePage.get_login_name(self))
        print("hii")
        print("999")




if __name__ == '__main__':
    unittest.main()
