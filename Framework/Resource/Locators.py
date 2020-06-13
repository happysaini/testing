from selenium.webdriver.common.by import By

class Locators():

    # --- Home Page Locators ---
    ADMIN_LINK = (By.XPATH, "//a[contains(text(),'Admin')]")
    STUDENT_LINK = (By.XPATH, "//a[contains(text(),'Student')]")
    ABOUT_US_LINK = (By.XPATH, "//a[contains(text(),'About Us')]")
    CONTACT_US_LINK =(By.XPATH, "//a[contains(text(),'Contact Us')]")

    # --- Admin Page Locators ---
    ADMIN_SIGN_UP = (By.XPATH, "//a[contains(text(),'SignUp')]")
    ADMIN_LOGIN = (By.XPATH, "//a[contains(text(),'Login')]")

    # --- Student Page Locators ---
    STUDENT_SIGN_UP = (By.XPATH, "//a[contains(text(),'SignUp')]")
    STUDENT_LOGIN = (By.XPATH, "//a[contains(text(),'Login')]")

    # --- Admin SignUp Page Locators ---
    ADMIN_SIGN_UP_FIRST_NAME = (By.ID, "id_first_name")
    ADMIN_SIGN_UP_LAST_NAME = (By.ID, "id_last_name")
    ADMIN_SIGN_UP_USER_NAME = (By.ID, "id_username")
    ADMIN_SIGN_UP_PASSWORD = (By.ID, "id_password")
    ADMIN_SIGN_UP_SUBMIT = (By.XPATH, "//button[@class='btn btn-primary btn-lg']")

    # --- Student SignUp Page Locators ---
    STUDENT_SIGN_UP_FIRST_NAME = (By.ID, "id_first_name")
    STUDENT_SIGN_UP_LAST_NAME = (By.ID, "id_last_name")
    STUDENT_SIGN_UP_USER_NAME = (By.ID, "id_username")
    STUDENT_SIGN_UP_PASSWORD = (By.ID, "id_password")
    STUDENT_SIGN_UP_ENROLLMENT = (By.ID, "id_enrollment")
    STUDENT_SIGN_UP_BRANCH = (By.ID, "id_branch")
    STUDENT_SIGN_UP_SUBMIT = (By.XPATH, "//button[@class='btn btn-primary btn-lg']")

    # --- Admin Login Page Locators ---
    ADMIN_LOGIN_USER_NAME = (By.ID, "id_username")
    ADMIN_LOGIN_PASSWORD = (By.ID, "id_password")
    ADMIN_LOGIN_SUBMIT = (By.XPATH, "//button[@class='btn btn-primary btn-lg']")

    # --- Student Login Page Locators ---
    STUDENT_LOGIN_USER_NAME = (By.ID, "id_username")
    STUDENT_LOGIN_PASSWORD = (By.ID, "id_password")
    STUDENT_LOGIN_SUBMIT = (By.XPATH, "//button[@class='btn btn-primary btn-lg']")

    # --- Student Login Page Locators ---
    STUDENT_VIEW_ISSUED_BOOKS = (By.XPATH, "//a[@class='btn btn-primary btn-lg active']")

    # --- Admin Logined Page Locators ---
    ADMIN_ADD_BOOK = (By.XPATH, "//a[contains(text(),'Add Book To Library')]")
    ADMIN_VIEW_BOOK = (By.XPATH, "//a[contains(text(),'View Available Book')]")
    ADMIN_ISSUE_BOOK = (By.XPATH, "//a[@class='btn btn-primary btn-lg active'][contains(text(),'Issue New Book')]")
    ADMIN_VIEW_ISSUED_BOOKS = (By.XPATH, "//a[@class='btn btn-primary btn-lg active'][contains(text(),'View Issued Book')]")
    ADMIN_VIEW_STUDENTS_LIST = (By.XPATH, "//a[@class='btn btn-primary btn-lg active'][contains(text(),'View Student')]")

    # --- Admin Logout Page Locators ---
    ADMIN_LOGOUT = (By.XPATH, "//a[contains(text(),'LOGOUT')]")

    # --- Student Logout Page Locators ---
    STUDENT_LOGOUT = (By.XPATH, "//a[contains(text(),'LOGOUT')]")

    # --- Add Book Page Locators ---
    ADD_BOOK_NAME = (By.ID, "id_name")
    ADD_BOOK_ISBN = (By.ID, "id_isbn")
    ADD_BOOK_AUTHOR = (By.ID, "id_author")
    ADD_BOOK_CATEGORY = (By.ID, "id_category")
    ADD_BOOK_SUBMIT = (By.XPATH, "//button[@class='btn btn-primary btn-lg']")

    # --- Issue Book Page Locators ---
    ISSUE_BOOK_NAME = (By.ID, "id_isbn2")
    ISSUE_STUDENT_NAME = (By.ID, "id_enrollment2")
    ISSUE_BOOK_SUBMIT = (By.XPATH, "//button[@class='btn btn-primary btn-lg']")