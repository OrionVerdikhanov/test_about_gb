from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
opts.add_argument("--headless")          # уберите строку, если нужен GUI
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opts)
print("Запущен Chrome:", driver.capabilities["browserVersion"])
driver.quit()
