import os

from pages.base import WebPage
from pages.elements import WebElement


class MailEmailPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://mail.ru/'

        super().__init__(web_driver, url)

    #Button write letter
    btn_write_letter = WebElement(css_selector='[class="compose-button__txt"]')

    #Field input address email
    f_address_email = WebElement(css_selector='[class="input--3slxg"]')

    #Field input text email
    f_text_email = WebElement()

    #Button send email
    btn_send_email = WebElement(css_selector='[class="vkuiButton__content"]')


