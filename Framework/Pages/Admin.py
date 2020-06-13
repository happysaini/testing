import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir + '\TestData')
sys.path.insert(0, parentdir + '\Resource')
sys.path.insert(0, parentdir + '\Controls')

from Reusable import update_iterator
from TestData import TestData
from Locators import Locators
from Base import BasePage

class Admin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def admin_Signup(self, data):
        self.click(Locators.ADMIN_LINK)
        self.click(Locators.ADMIN_SIGN_UP)
        self.driver.find_element(*Locators.ADMIN_SIGN_UP_FIRST_NAME).clear()
        self.enter_text(Locators.ADMIN_SIGN_UP_FIRST_NAME, data.get("fname", "") + str(TestData.ADMIN_ITERATOR))
        self.driver.find_element(*Locators.ADMIN_SIGN_UP_LAST_NAME).clear()
        self.enter_text(Locators.ADMIN_SIGN_UP_LAST_NAME, data.get("lname", ""))
        self.driver.find_element(*Locators.ADMIN_SIGN_UP_USER_NAME).clear()
        self.enter_text(Locators.ADMIN_SIGN_UP_USER_NAME, data.get("username", "") + str(TestData.ADMIN_ITERATOR))
        self.driver.find_element(*Locators.ADMIN_SIGN_UP_PASSWORD).clear()
        self.enter_text(Locators.ADMIN_SIGN_UP_PASSWORD, data.get("password", ""))
        self.click(Locators.ADMIN_SIGN_UP_SUBMIT)
        update_iterator("ADMIN_ITERATOR", TestData.ADMIN_ITERATOR)

    def admin_Login(self, data):
        self.click(Locators.ADMIN_LINK)
        self.click(Locators.ADMIN_LOGIN)
        self.driver.find_element(*Locators.ADMIN_LOGIN_USER_NAME).clear()
        self.enter_text(Locators.ADMIN_LOGIN_USER_NAME, data.get("username", "") + str(TestData.ADMIN_ITERATOR -1))
        self.driver.find_element(*Locators.ADMIN_LOGIN_PASSWORD).clear()
        self.enter_text(Locators.ADMIN_LOGIN_PASSWORD, data.get("password", ""))
        self.click(Locators.ADMIN_LOGIN_SUBMIT)

    def admin_Logout(self):
        self.click(Locators.ADMIN_LOGOUT)

    def __del__(self):
        self.driver.close()

