from pages.base import WebPage
from pages.elements import WebElement


class MailAuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://account.mail.ru/login/?mode=simple&v=2.10.1&account_host=account.mail.ru&type=login&' \
              'allow_external=1&app_id_mytracker=58519&success_redirect=https%3A%2F%2Fe.mail.ru%2Fmessages%2Finbox%3Fback%3D1&project=home&source=mailbox&from=navi&parent_url=https%3A%2F%2Fmail.ru%2F&responsive=compact'
        super().__init__(web_driver, url)

    # Field for enter name user
    f_user_name = WebElement(css_selector='[data-test-id="login-app-ready"] [name="username"]')

    # Button enter password
    btn_enter_pass = WebElement(css_selector="button[data-test-id='next-button']")

    # Field for enter password
    f_user_password = WebElement(css_selector="input[name='password']")

    # Button login in account
    btn_login_account = WebElement(css_selector="[data-test-id='submit-button']")

    # Button write letter
    btn_write_letter = WebElement(css_selector='[class="compose-button__txt"]')

    # Field input address email
    f_address_email = WebElement(css_selector='[class="input--3slxg"]')