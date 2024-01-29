"""
import pytest
from pages.mail_auth import MailAuthPage

USER_NAME = ""
PASSWORD = ""

def test_authorisation(web_browser):

    page = MailAuthPage(web_browser)

    page.f_user_name.send_keys(USER_NAME)

    page.btn_enter_pass.click()

    page.f_user_password.send_keys(PASSWORD)

    page.btn_login_account.click()

    page.btn_write_letter.click()

    page.f_address_email.send_keys(USER_NAME)
"""