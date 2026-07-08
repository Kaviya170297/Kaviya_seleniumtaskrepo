from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    username_txt= (By.NAME, "username")
    password_txt= (By.NAME, "password")
    login_btn= (By.XPATH, "//button[normalize-space()='Login']")
    dashboard_header= (By.XPATH, "//h6[normalize-space()='Dashboard']")
    dropdown = (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    logout_link =(By.XPATH, "//a[normalize-space()='Logout']")
    error_msg= (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        username_field = self.wait.until(EC.visibility_of_element_located(self.username_txt))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.password_txt))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_successful_login(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.dashboard_header))
            return True
        except:
            return False

    def logout(self):
        self.wait.until(EC.visibility_of_element_located(self.dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()