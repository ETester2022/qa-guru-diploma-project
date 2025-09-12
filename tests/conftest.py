import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa_guru_diploma_project.utils import attach
from dotenv import load_dotenv
import requests
from qa_guru_diploma_project.utils.utils import reqres_post


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        },
        "goog:loggingPrefs": {"browser": "ALL"}
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    url = os.getenv('URL')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{url}",
        options=options
    )
    driver.set_window_size(1920, 1080)

    yield driver

    attach.add_screenshot(driver)
    attach.add_logs(driver)
    attach.add_html(driver)
    attach.add_video(driver)
    driver.quit()


@pytest.fixture()
def get_access_token_admin():
    login_admin = os.getenv('LOGIN_ADMIN')
    password_admin = os.getenv('PASSWORD_ADMIN')
    base_url_api = os.getenv('BASE_URL_API')
    creds = {
        "username": login_admin,
        "password": password_admin
    }
    response = requests.post(base_url_api + '/user/login', json=creds)
    access_token = response.json()["accessToken"]
    return access_token


@pytest.fixture()
def get_access_token_not_admin():
    login_user = os.getenv('LOGIN_USER')
    password_user = os.getenv('PASSWORD_USER')
    base_url_api = os.getenv('BASE_URL_API')
    creds = {
        "username": login_user,
        "password": password_user
    }
    response = requests.post(base_url_api + '/user/login', json=creds)
    access_token = response.json()["accessToken"]
    return access_token


@pytest.fixture()
def refresh_token_admin():
    url = '/user/login'
    login_admin = os.getenv('LOGIN_ADMIN')
    password_admin = os.getenv('PASSWORD_ADMIN')
    request_body = {
        "username": f"{login_admin}",
        "password": f"{password_admin}"
    }

    response = reqres_post(url, json=request_body)
    cookie = response.cookies.get("refreshToken")

    return cookie


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
