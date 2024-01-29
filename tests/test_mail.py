import pytest
from pages.mail import MainPage

BASE_URL = "https://mail.ru/"
EMAIL_ADDRESS = "solomin@211.ru"

def test_send_email(web_browser):

    page = MainPage(web_browser)

    page.wait_page_loaded()

    page.btn_enter.click()

    #page.wait_page_loaded()

    page.switch_to_window()

    page.f_user_name.click()

    page.f_user_name = USER_NAME

    page.btn_enter_pass.click()

    page.f_user_password.send_keys(PASSWORD)

    page.btn_login_account.click()
