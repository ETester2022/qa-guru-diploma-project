import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa_guru_diploma_project.utils import attach
from dotenv import load_dotenv
from qa_guru_diploma_project.utils.application import Application
import requests


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
def delete_tool_crud_auto(get_access_token_admin):
    yield
    name = "crud_auto"
    requests.delete(f'https://stage.mesone.kz/api/v1/tools/{name}',
                    headers={"Authorization": f"Bearer {get_access_token_admin}"})


@pytest.fixture()
def create_crud_auto(get_access_token_admin):
    name = "crud_auto"
    request_body = {
        "name": f"{name}",
        "type": "crud"
    }
    response = requests.post('https://stage.mesone.kz/api/v1/tools',
                             headers={"Authorization": f"Bearer {get_access_token_admin}"},
                             json=request_body)
    return response.json()["name"]
