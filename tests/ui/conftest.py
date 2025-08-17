import os
import pytest
from allure_commons import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa_guru_diploma_project.utils import attach
from dotenv import load_dotenv
from qa_guru_diploma_project.utils.application import Application
import requests
from tests.api.application_settings import data_app_settings_api


@pytest.fixture()
def default_upload_picture(get_access_token_admin):
    """Фикстура отключает Изображение и удаляет Картинку"""
    request_body = {
        "commonSettings": {
            "logoEnabled": False,
            "logoImage": None
        }
    }

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.patch(base_url_api + '/application/settings',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=request_body)
    return response


@pytest.fixture()
def add_picture(get_access_token_admin):
    """Фикстура включает Изображение и добавляет Картинку(PNG)"""

    request_body = {
        "commonSettings": {
            "logoEnabled": True,
            "logoImage": data_app_settings_api.logo_png
        }
    }

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.patch(base_url_api + '/application/settings',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=request_body)
    return response


@pytest.fixture()
def default_main_text_en(get_access_token_admin):
    """Фикстура отключает Текст и очищает поле Основной(EN)"""

    request_body = {
        "commonSettings": {
            "instanceLabelEnabled": False,
            "instanceLabel": {
                "en": ""
            }
        }
    }

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.patch(base_url_api + '/application/settings',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=request_body)
    return response


@pytest.fixture()
def style_light(get_access_token_admin):
    """Фикстура устанавливает стиль Светлый и включает Футер"""

    request_body = {
        "commonSettings": {
            "style": "light",
            "footer": True
        }
    }

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.patch(base_url_api + '/application/settings',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=request_body)
    return response


@pytest.fixture()
def theme_default(get_access_token_admin):
    """Фикстура устанавливает Тема Default()"""
    request_body = {
        "commonSettings": {
            "colorScheme": "default"
        }
    }
    base_url_api = os.getenv('BASE_URL_API')
    response = requests.patch(base_url_api + '/application/settings',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=request_body)
    return response


@pytest.fixture()
def disabling_footer(get_access_token_admin):
    """Фикстура отключает Футер"""

    request_body = {
        "commonSettings": {
            "footer": False
        }
    }

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.patch(base_url_api + '/application/settings',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=request_body)
    return response
