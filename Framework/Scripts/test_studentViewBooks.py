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

from Student_Homepage import StudentHomePage
from TestData import TestData

class Test_student_view_book:
    @pytest.fixture
    def setUp(self):
        self.student = StudentHomePage(webdriver.Firefox())
        yield
        del self.student

    def test_studentViewBook(self, setUp):
        self.student.student_View_Book(TestData.STUDENT_DATA)
        time.sleep(2)
