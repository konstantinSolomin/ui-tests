import pytest
import allure
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.fixture
def web_browser(request, selenium):

    service = Service()
    options = webdriver.ChromeOptions()

    browser = webdriver.Chrome(service=service, options=options)
    browser.set_window_size(1400, 1000)

    # Return browser instance to test case:
    yield browser

    # Do tear down (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screenshot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screenshot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Attach screenshot to Allure report:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here
