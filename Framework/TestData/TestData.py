import random

class TestData():
    BASE_URL = "http://localhost:8000/"
    CHROME_EXECUTABLE_PATH = "D:/office/demo_apps/library/selenium_test_cases/Framework/Drivers/chromedriver.exe"
    ADMIN_DATA = {"fname": "admin",
    "lname": "admin",
    "username": "admin",
    "password": "admin123"}

    STUDENT_DATA = {"fname": "student",
    "lname": "student",
    "username": "student",
    "password": "student123",
    "enrollment": 100,
    "branch": random.randint(1, 9)}

    BOOK_DATA ={"name": "book",
    "isbn": 10002,
    "author": "author",
    "category": random.choice(["Education", "Entertainment", "Comics", "Biographie", "History"])}

    ADMIN_ITERATOR = 1006
    STUDENT_ITERATOR = 1006
    BOOK_ITERATOR = 1008