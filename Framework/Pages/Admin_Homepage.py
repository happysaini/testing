import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir + '\Pages')
sys.path.insert(0, parentdir + '\TestData')
sys.path.insert(0, parentdir + '\Resource')
sys.path.insert(0, parentdir + '\Controls')

from Reusable import update_iterator
from TestData import TestData
from Locators import Locators
from Admin import Admin

class AdminHomePage(Admin):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def admin_Add_Book(self, admin_data, book_data):
        self.admin_Login(admin_data)
        self.click(Locators.ADMIN_ADD_BOOK)
        self.driver.find_element(*Locators.ADD_BOOK_NAME).clear()
        self.enter_text(Locators.ADD_BOOK_NAME, book_data.get("name", "") + str(TestData.BOOK_ITERATOR))
        self.driver.find_element(*Locators.ADD_BOOK_ISBN).clear()
        self.enter_text(Locators.ADD_BOOK_ISBN, book_data.get("isbn", "") + TestData.BOOK_ITERATOR)
        self.driver.find_element(*Locators.ADD_BOOK_AUTHOR).clear()
        self.enter_text(Locators.ADD_BOOK_AUTHOR, book_data.get("author", "") + str(TestData.BOOK_ITERATOR))
        self.select(Locators.ADD_BOOK_CATEGORY, book_data.get("category", ""))
        self.click(Locators.ADD_BOOK_SUBMIT)
        update_iterator("BOOK_ITERATOR", TestData.BOOK_ITERATOR)


    def admin_Issue_Book(self, admin_data, book_data, student_data):
        book_name_and_isbn = book_data.get("name", "")+str(TestData.BOOK_ITERATOR-1)+"["+str((book_data.get("isbn", "")+TestData.BOOK_ITERATOR)-1)+"]"
        student_name_and_enrollment = student_data.get("fname","")+str(TestData.STUDENT_ITERATOR-1)+"["+str((student_data.get("enrollment", "")+TestData.STUDENT_ITERATOR)-1)+"]"
        self.admin_Login(admin_data)
        self.click(Locators.ADMIN_ISSUE_BOOK)
        self.select(Locators.ISSUE_BOOK_NAME, book_name_and_isbn)
        self.select(Locators.ISSUE_STUDENT_NAME, student_name_and_enrollment)
        self.click(Locators.ISSUE_BOOK_SUBMIT)

    def admin_View_Book(self, admin_data):
        self.admin_Login(admin_data)
        self.click(Locators.ADMIN_VIEW_BOOK)

    def admin_View_Issued_Book(self, admin_data):
        self.admin_Login(admin_data)
        self.click(Locators.ADMIN_VIEW_ISSUED_BOOKS)

    def admin_View_Students_List(self, admin_data):
        self.admin_Login(admin_data)
        self.click(Locators.ADMIN_VIEW_STUDENTS_LIST)

