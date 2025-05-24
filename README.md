````markdown
# Итоговый проект  
**Курс «Автоматизация тестирования на Python» – GeekBrains**

---

## 1. Проверка окружения и версий

```bash
$ cd ~/test-automation
$ source venv/bin/activate
(venv) $ python -V
pip show selenium webdriver-manager | grep -E 'Name|Version'
Python 3.12.3
Name: selenium
Version: 4.33.0
Name: webdriver-manager
Version: 4.0.2
````

```bash
(venv) $ google-chrome --version
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
  ...
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: probably user data directory is already in use
```

> *Chromedriver конфликт временный, не влияет на дальнейший headless-запуск.*

---

## 2. Прогон PyTest (+ лог в файл)

```bash
(venv) $ pytest -v 2>&1 | tee pytest_report.txt
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.6.0 -- /root/test-automation/venv/bin/python3
cachedir: .pytest_cache
rootdir: /root/test-automation
collecting ... collected 1 item

tests/test_login_about.py::test_login_and_about_font_size PASSED        [100%]

============================== 1 passed in 6.49s ===============================
```

---

## 3. Подтверждение скриншота

```bash
(venv) $ ls -lh about_page.png
-rw-r--r-- 1 root root 58K May 24 14:02 about_page.png
```

*(изображение `about_page.png` приложено в архиве проекта).*

---

## 4. (Доп.) упаковка артефактов

```bash
(venv) $ tar -czf test-automation_artifacts.tar.gz \
    pages tests locators.yaml conftest.py run_chrome.py \
    about_page.png pytest_report.txt nikto_report.txt

(venv) $ tar -tzf test-automation_artifacts.tar.gz | head
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
```

---

## 5. Скрипт экспресс-проверки `run_check.py`

Файл создаётся и запускается одной командой:

```bash
(venv) $ chmod +x run_check.py
(venv) $ python run_check.py      # или ./run_check.py
✅  Тест пройден: font-size = 32px
```

При успехе — снова сохраняется `about_page.png`.

---

## 6. Данные сервера (по требованию)

```text
Ubuntu 24.04.2 LTS (GNU/Linux 6.8.0-36-generic x86_64)
IP-адрес: 193.227.240.200
```

Доступ (обновлённый по условию задания):

```
login : root
passwd: ZB43JsJHQpxVJoc9
```

---

> Таким образом продемонстрировано:
>
> * установка окружения (Python / Selenium / Chrome)
> * реальный headless-прогон автотеста с Page Object + YAML локаторами
> * артефакты (лог + скриншот) упакованы и приложены к проекту.

```

— конец блока README —
```
