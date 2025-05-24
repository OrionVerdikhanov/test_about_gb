root@cv4815907:~# cd ~/test-automation
root@cv4815907:~/test-automation# source venv/bin/activate
(venv) root@cv4815907:~/test-automation# python -V
pip show selenium webdriver-manager | grep -E 'Name|Version'
Python 3.12.3
Name: selenium
Version: 4.33.0
Name: webdriver-manager
Version: 4.0.2
(venv) root@cv4815907:~/test-automation# google-chrome --version
python - <<'PY'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
svc = Service(ChromeDriverManager().install())
drv = webdriver.Chrome(service=svc)
print("Chromedriver version:", drv.capabilities["browserVersion"])
drv.quit()
PY
Google Chrome 136.0.7103.113 
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  File "/root/test-automation/venv/lib/python3.12/site-packages/selenium/webdriver/chrome/webdriver.py", line 47, in __init__
    super().__init__(
  File "/root/test-automation/venv/lib/python3.12/site-packages/selenium/webdriver/chromium/webdriver.py", line 69, in __init__
    super().__init__(command_executor=executor, options=options)
  File "/root/test-automation/venv/lib/python3.12/site-packages/selenium/webdriver/remote/webdriver.py", line 257, in __init__
    self.start_session(capabilities)
  File "/root/test-automation/venv/lib/python3.12/site-packages/selenium/webdriver/remote/webdriver.py", line 356, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/test-automation/venv/lib/python3.12/site-packages/selenium/webdriver/remote/webdriver.py", line 447, in execute
    self.error_handler.check_response(response)
  File "/root/test-automation/venv/lib/python3.12/site-packages/selenium/webdriver/remote/errorhandler.py", line 232, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: probably user data directory is already in use, please specify a unique value for --user-data-dir argument, or don't use --user-data-dir
Stacktrace:
#0 0x55972ef9d71a <unknown>
#1 0x55972ea400a0 <unknown>
#2 0x55972ea7a1ff <unknown>
#3 0x55972ea75c0f <unknown>
#4 0x55972eac5d75 <unknown>
#5 0x55972eac5296 <unknown>
#6 0x55972eab7173 <unknown>
#7 0x55972ea83d4b <unknown>
#8 0x55972ea849b1 <unknown>
#9 0x55972ef628cb <unknown>
#10 0x55972ef667ca <unknown>
#11 0x55972ef4a622 <unknown>
#12 0x55972ef67354 <unknown>
#13 0x55972ef2f45f <unknown>
#14 0x55972ef8b4f8 <unknown>
#15 0x55972ef8b6d6 <unknown>
#16 0x55972ef9c586 <unknown>
#17 0x76a8d4e9caa4 <unknown>
#18 0x76a8d4f29c3c <unknown>

(venv) root@cv4815907:~/test-automation# pytest -v 2>&1 | tee pytest_report.txt
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.6.0 -- /root/test-automation/venv/bin/python3
cachedir: .pytest_cache
rootdir: /root/test-automation
collecting ... collected 1 item

tests/test_login_about.py::test_login_and_about_font_size ls -lh about_page.png
PASSED         [100%]

============================== 1 passed in 6.49s ===============================
(venv) root@cv4815907:~/test-automation# ls -lh about_page.png
-rw-r--r-- 1 root root 58K May 24 14:02 about_page.png
(venv) root@cv4815907:~/test-automation# nikto -h https://test-stand.gb.ru/ -ssl -Tuning 4 | tee nikto_report.txt
grep "0 error(s)" nikto_report.txt
-bash: nikto: command not found
(venv) root@cv4815907:~/test-automation# tar -czf test-automation_artifacts.tar.gz \
    pages tests locators.yaml conftest.py run_chrome.py \
    about_page.png pytest_report.txt nikto_report.txt
(venv) root@cv4815907:~/test-automation# tar -tzf test-automation_artifacts.tar.gz | head
pages/
pages/__pycache__/
pages/__pycache__/about_page.cpython-312.pyc
pages/__pycache__/login_page.cpython-312.pyc
pages/login_page.py
pages/about_page.py
tests/
tests/test_login_about.py
tests/__pycache__/
tests/__pycache__/test_login_about.cpython-312-pytest-8.3.5.pyc
(venv) root@cv4815907:~/test-automation# Welcome to Ubuntu 24.04.2 LTS (GNU/Linux 6.8.0-36-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sat May 24 02:04:11 PM MSK 2025

  System load:  0.1               Processes:             101
  Usage of /:   31.4% of 9.76GB   Users logged in:       0
  Memory usage: 24%               IPv4 address for ens3: 192.168.0.34
  Swap usage:   0%


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


*** System restart required ***
Last login: Sat May 24 14:01:05 2025 from 62.60.247.115
root@cv4815907:~# cd ~/test-automation
root@cv4815907:~/test-automation# source venv/bin/activate
(venv) root@cv4815907:~/test-automation# ##############################################################################
# 1. Создаём/перезаписываем run_check.py
##############################################################################
cat > run_check.py << 'EOF'
#!/usr/bin/env python3
"""
Проверка задания: логин → About → шрифт = 32px.
Результат печатается в консоль, код выхода 0 (OK) или 1 (FAIL).
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import sys, yaml, textwrap

# ----- настройки ------------------------------------------------------------
LOGIN    = "GB202310991172"
PASSWORD = "12ba98fc66"
BASE_URL = "https://test-stand.gb.ru"
# локаторы берём из YAML (если файла нет, берём дефолтные)
loc = {
    "username": "form#login input[type='text']",
    "password": "form#login input[type='password']",
    "submit":   "form#login button[type='submit']",
    "about":    "nav a[href='/about']",
    "header":   "main h1"
}
try:
    loc.update(yaml.safe_load(open("locators.yaml"))["login_page"])
    about = yaml.safe_load(open("locators.yaml"))["about_page"]
    loc["about"]  = about["about_link"]
    loc["header"] = about["header"]
except Exception:
    pass
# ---------------------------------------------------------------------------

def main():
    opts = Options()
    opts.add_argument("--headless")
python run_check.py   # или ./run_check.py####################################OR, loc["
✅  Тест пройден: font-size = 32px 

Данные от сервера Ubuntu 
Вы установили Ubuntu 24.04 LTS на сервер Тестирование для ГБ. IP адрес 193.227.240.200
Новый доступ к серверу
Логин: root
Пароль: ZB43JsJHQpxVJoc9

