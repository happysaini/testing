import time
from selenium import webdriver
import os, sys, inspect
import pytest
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir + '\Pages')
sys.path.insert(0, parentdir + '\TestData')

from Admin_Homepage import AdminHomePage
from TestData import TestData

class Test_admin_issue_book:
    @pytest.fixture
    def setUp(self):
        self.admin = AdminHomePage(webdriver.Firefox())
        yield
        del self.admin

    def test_adminIssuedBook(self, setUp):
        self.admin.admin_Issue_Book(TestData.ADMIN_DATA, TestData.BOOK_DATA, TestData.STUDENT_DATA)
        time.sleep(4)
        self.admin.admin_Logout()
