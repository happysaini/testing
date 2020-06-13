import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir + '\Pages')
sys.path.insert(0, parentdir + '\TestData')
sys.path.insert(0, parentdir + '\Resource')

from TestData import TestData
from Locators import Locators
from Student import Student

class StudentHomePage(Student):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def student_View_Book(self, student_data):
        self.student_Login(student_data)
        self.click(Locators.STUDENT_VIEW_ISSUED_BOOKS)


