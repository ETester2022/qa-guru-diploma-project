import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa_guru_diploma_project.utils import attach
from dotenv import load_dotenv
from qa_guru_diploma_project.utils.application import Application
# from qa_guru_diploma_project.model.pages.web.user_login_page import UserLoginPage
# from qa_guru_diploma_project.model.pages.web.application_page import SettingsAppPage


# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()
#
#
# @pytest.fixture(scope='function')
# def browser():
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "128.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True,
#             "enableLog": True
#         },
#         "goog:loggingPrefs": {"browser": "ALL"}
#     }
#     options.capabilities.update(selenoid_capabilities)
#
#     login = os.getenv('LOGIN')
#     password = os.getenv('PASSWORD')
#     url = os.getenv('URL')
#
#     driver = webdriver.Remote(
#         command_executor=f"https://{login}:{password}@{url}",
#         options=options
#     )
#     driver.set_window_size(1920, 1080)
#
#     yield driver
#
#     attach.add_screenshot(driver)
#     attach.add_logs(driver)
#     attach.add_html(driver)
#     attach.add_video(driver)
#     driver.quit()

@pytest.fixture()
def browser():
    """Фикстура для создания драйвера браузера."""

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture()
def auth_admin(browser):

    app = Application(browser)
    # выделить в фикстуру авторизация admin
    app.login_page.open_user_login_page()
    app.login_page.filling_login('admin')
    app.login_page.filling_password('admin')
    app.login_page.click_login_btn()

    return browser


# @pytest.fixture()
# def auth_admin(browser):
#     app = Application(browser)
#     app.open_user_login_page()
#     app.filling_login('admin')
#     app.filling_password('admin')
#     app.click_login_btn()