import os
import pytest
import requests
from tests.api.test_application_settings import data_app_settings_api


@pytest.fixture()
def create_crud(get_access_token_admin):

    tool_name = "create_name"
    request_body = {
        "name": tool_name,
        "type": "crud"
    }

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.post(base_url_api + '/tools',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=request_body)
    yield response

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.delete(base_url_api + f'/tools/{tool_name}',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=request_body)
    return response

@pytest.fixture()
def create_crud_with_settings_table(get_access_token_admin):

    tool_name = "create_name"
    post_request_body = {
        "name": tool_name,
        "type": "crud"
    }
    patch_request_body = {
      "toolSettings": {
        "frozenTopEnabled": True,
        "frozenTopCount": 1,
        "frozenLeftEnabled": True,
        "frozenLeftCount": 1,
        "frozenRightEnabled": True,
        "frozenRightCount": 1,
        "exportCsv": True,
        "exportJson": True,
        "exportXlsx": True,
        "exportPdf": True,
        "importCsv": True,
        "importJson": True,
        "fontSize": 12,
        "rowHeight": 12,
        "fitToWidth": True,
        "paginationEnabled": True,
        "paginationRows": 10
      }
    }

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.post(base_url_api + '/tools',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=post_request_body)
    requests.patch(base_url_api + f'/tools/{tool_name}',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=patch_request_body)
    yield response

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.delete(base_url_api + f'/tools/{tool_name}',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=post_request_body)
    return response

@pytest.fixture()
def create_crud_with_fields(get_access_token_admin):

    tool_name = "create_name"
    post_request_body = {
        "name": tool_name,
        "type": "crud"
    }
    patch_request_body = {
      "toolSettings": {
        "source": "dflt.cities",
        "crudFields": [
            {"fieldName": "dflt.cities.id",
            "enabled": True},
            {"fieldName": "dflt.cities.name",
             "enabled": True},
            {"fieldName": "dflt.cities.population",
             "enabled": True},
        ]
      }
    }

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.post(base_url_api + '/tools',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=post_request_body)
    requests.patch(base_url_api + f'/tools/{tool_name}',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=patch_request_body)
    yield response

    base_url_api = os.getenv('BASE_URL_API')
    response = requests.delete(base_url_api + f'/tools/{tool_name}',
                              headers={"Authorization": f"Bearer {get_access_token_admin}"},
                              json=post_request_body)
    return response