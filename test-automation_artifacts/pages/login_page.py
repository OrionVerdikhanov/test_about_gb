import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://test-stand.gb.ru/login"      # точный путь к форме

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        loc = yaml.safe_load(open("locators.yaml"))["login_page"]
        self.username = (By.CSS_SELECTOR, loc["username"])
        self.password = (By.CSS_SELECTOR, loc["password"])
        self.submit   = (By.CSS_SELECTOR, loc["submit"])

    def open(self):
        self.driver.get(self.URL)

    def login(self, user, pwd):
        self.wait.until(EC.element_to_be_clickable(self.username)).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.submit).click()
