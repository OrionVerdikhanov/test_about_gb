from pages.login_page import LoginPage
from pages.about_page import AboutPage

def test_login_and_about_font_size(driver):
    lp = LoginPage(driver)
    ap = AboutPage(driver)

    lp.open()
    lp.login(user="GB202310991172", pwd="12ba98fc66")

    ap.go_to()
    size = ap.header_font_size()
    assert size == "32px", f"Ожидали 32 px, получили {size}"

    # скриншот в случае успеха (можно убрать)
    driver.save_screenshot("about_page.png")
