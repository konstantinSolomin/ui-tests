import os

from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://mail.ru/'

        super().__init__(web_driver, url)

    #Button enter in account
    btn_enter = WebElement(xpath='//*[@id="ph-whiteline"]/div/nav/ul/li[2]/a')

    #Field for enter name user
    f_user_name = WebElement(name='username')

    # Button enter password
    btn_enter_pass = WebElement(css_selector="button[data-test-id='next-button']")

    #Field for enter password
    f_user_password = WebElement(css_selector="input[name='password']")

    #Button login in account
    btn_login_account = WebElement(css_selector="[data-test-id='submit-button']")

    #Button send email
    btn_send_email = WebElement(class_name="compose-button__wrapper")

    #Field for enter email address
    f_email_address = WebElement(css_selector="div[class='input--3slxg'] input[class='container--H9L5q size_s--3_M-_']")

    #Field for enter email topic
    f_email_topic = WebElement(css_selector="div[class='container--3QXHv'] "
                                            "input[class='container--H9L5q size_s--3_M-_']")

    #Field for enter mail text
    f_email_text = ()

    #Frame login account
    frame = WebElement(css_selector='[class="wrapper-0-2-5"]')

