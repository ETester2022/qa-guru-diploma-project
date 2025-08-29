import os
import logging
import requests
import json
import allure
from allure_commons.types import AttachmentType


def get_picture_path(filename):
    """Возвращает абсолютный путь к картинке в tests/resources."""
    base_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(base_dir, '..', '..'))  # поднимаемся к корню проекта
    resources_dir = os.path.join(project_root, 'tests', 'resources')
    picture_path = os.path.join(resources_dir, filename)

    if not os.path.isfile(picture_path):
        raise FileNotFoundError(f"Файл {filename} не найден в {resources_dir}")
    return picture_path


def reqres_get(url, **kwargs):
    """Выполняет GET-запрос"""
    base_url_api = os.getenv('BASE_URL_API')
    result = requests.get(base_url_api + url, **kwargs)
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")

    logging.info(result.request.url)
    logging.info(result.request.headers)
    logging.info(result.request.body)

    logging.info(result.status_code)
    logging.info(result.text)

    return result


def reqres_post(url, **kwargs):
    """Выполняет POST-запрос"""
    base_url_api = os.getenv('BASE_URL_API')
    result = requests.post(base_url_api + url, **kwargs)
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")

    logging.info(result.request.url)
    logging.info(result.request.headers)
    logging.info(result.request.body)

    logging.info(result.status_code)
    logging.info(result.text)

    return result


def reqres_patch(url, **kwargs):
    """Выполняет PATCH-запрос"""
    base_url_api = os.getenv('BASE_URL_API')
    result = requests.patch(base_url_api + url, **kwargs)
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")

    logging.info(result.request.url)
    logging.info(result.request.headers)
    logging.info(result.request.body)

    logging.info(result.status_code)
    logging.info(result.text)

    return result


def reqres_delete(url, **kwargs):
    """Выполняет DELETE-запрос"""
    base_url_api = os.getenv('BASE_URL_API')
    result = requests.delete(base_url_api + url, **kwargs)

    # allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
    #               attachment_type=AttachmentType.JSON, extension="json")
    #
    # Нужно доработать attach, тест падает при отсутствии body в response

    logging.info(result.request.url)
    logging.info(result.request.headers)
    logging.info(result.request.body)

    logging.info(result.status_code)
    logging.info(result.text)

    return result
