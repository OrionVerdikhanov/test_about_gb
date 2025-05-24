import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AboutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        loc = yaml.safe_load(open("locators.yaml"))["about_page"]
        self.about_link = (By.CSS_SELECTOR, loc["about_link"])
        self.header     = (By.CSS_SELECTOR, loc["header"])

    def go_to(self):
        self.wait.until(EC.element_to_be_clickable(self.about_link)).click()

    def header_font_size(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.header))
        return elem.value_of_css_property("font-size")
