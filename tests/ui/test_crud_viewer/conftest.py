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
        "exportCsv": True,
        "exportJson": True,
        "exportXlsx": True,
        "exportPdf": True,
        "importCsv": True,
        "importJson": True,
        "fontSize": 12,
        "rowHeight": 25,
        "fitToWidth": True,
        "paginationEnabled": True,
        "paginationRows": 10,
        "staticCreate": True,
        "staticUpdate": True,
        "staticDelete": True,
        "paginationPosition": "up",
        "source": "dflt.cities",
        "crudFields": [
            {
                "crudName": "RELEASE_CRUD",
                "fieldName": "dflt.cities.name",
                "enabled": True,
                "position": 1,
                "h": 2,
                "i": "dflt.cities.name",
                "w": 3,
                "x": 0,
                "y": 0
            },
            {
                "crudName": "RELEASE_CRUD",
                "fieldName": "dflt.cities.population",
                "enabled": True,
                "position": 3,
                "h": 4,
                "i": "dflt.cities.population",
                "w": 3,
                "x": 0,
                "y": 2
            }
        ]
      }
    }

    base_url_api = os.getenv('BASE_URL_API')
    resp_post_tool = requests.post(base_url_api + '/tools',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=post_request_body)
    resp_patch_tool = requests.patch(base_url_api + f'/tools/{tool_name}',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=patch_request_body)

    yield resp_post_tool

    base_url_api = os.getenv('BASE_URL_API')
    requests.delete(base_url_api + f'/tools/{tool_name}',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=post_request_body)

@pytest.fixture()
def create_crud_with_settings_table_fix(get_access_token_admin):

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
        "rowHeight": 25,
        "fitToWidth": True,
        "paginationEnabled": True,
        "paginationRows": 10,
        "paginationPosition": "up",
        "source": "dflt.cities",
        "crudFields": [
            {"fieldName": "dflt.cities.name",
             "enabled": True},
            {"fieldName": "dflt.cities.population",
             "enabled": True},
            {"fieldName": "dflt.cities.coordinates",
             "enabled": True}
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

@pytest.fixture()
def create_crud_all_settings_table_false(get_access_token_admin):

    tool_name = "create_name"
    post_request_body = {
        "name": tool_name,
        "type": "crud"
    }
    patch_request_body = {
      "toolSettings": {
        "exportCsv": False,
        "exportJson": False,
        "exportXlsx": False,
        "exportPdf": False,
        "importCsv": False,
        "importJson": False,
        "fontSize": 12,
        "rowHeight": 25,
        "fitToWidth": False,
        "paginationEnabled": False,
        "paginationRows": 10,
        "paginationPosition": "up",
        "source": "dflt.cities",
        "crudFields": [
            {"fieldName": "dflt.cities.name",
             "enabled": True},
            {"fieldName": "dflt.cities.population",
             "enabled": True},
            {"fieldName": "dflt.cities.coordinates",
             "enabled": True}
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

@pytest.fixture()
def create_crud_with_settings_and_record(get_access_token_admin):

    tool_name = "create_name"
    post_request_body = {
        "name": tool_name,
        "type": "crud"
    }
    patch_request_body = {
      "toolSettings": {
        "exportCsv": True,
        "exportJson": True,
        "exportXlsx": True,
        "exportPdf": True,
        "importCsv": True,
        "importJson": True,
        "fontSize": 12,
        "rowHeight": 25,
        "fitToWidth": True,
        "paginationEnabled": False,
        "paginationRows": 10,
        "staticCreate": True,
        "staticUpdate": True,
        "staticDelete": True,
        "paginationPosition": "up",
        "source": "dflt.rivers",
        "crudFields": [
            {
                "crudName": f"{tool_name}",
                "fieldName": "dflt.rivers.name",
                "enabled": True,
                "position": 1,
                "h": 2,
                "i": "dflt.rivers.name",
                "w": 3,
                "x": 0,
                "y": 0
            },
            {
                "crudName": f"{tool_name}",
                "fieldName": "dflt.rivers.length",
                "enabled": False,
                "position": 2,
                "h": 2,
                "i": "dflt.rivers.length",
                "w": 1,
                "x": 0,
                "y": 4
            },
            {
                "crudName": f"{tool_name}",
                "fieldName": "dflt.rivers.flow_rate",
                "enabled": True,
                "position": 3,
                "h": 4,
                "i": "dflt.rivers.flow_rate",
                "w": 3,
                "x": 0,
                "y": 2
            }
        ]
      }
    }

    post_body_record = {
      "data": {
        "name": "Исеть",
        "length": "170000",
        "flow_rate": "20"
      }
    }

    base_url_api = os.getenv('BASE_URL_API')
    resp_post_tool = requests.post(base_url_api + '/tools',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=post_request_body)
    requests.patch(base_url_api + f'/tools/{tool_name}',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=patch_request_body)
    resp_post_record = requests.post(base_url_api + f'/tools/{tool_name}/crud',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=post_body_record)
    
    id_record = resp_post_record.json()['data']['id']
    name_record = resp_post_record.json()['data']['name']
    params = {
      "pks[id]": id_record,
      "pks[name]": name_record
      }

    yield resp_post_tool

    base_url_api = os.getenv('BASE_URL_API')
    requests.delete(base_url_api + f'/tools/{tool_name}/crud',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  params=params)
    requests.delete(base_url_api + f'/tools/{tool_name}',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=post_request_body)

    return resp_post_tool

@pytest.fixture()
def create_crud_for_add_record(get_access_token_admin):

    tool_name = "create_name"
    post_request_body = {
        "name": tool_name,
        "type": "crud"
    }
    patch_request_body = {
      "toolSettings": {
        "exportCsv": True,
        "exportJson": True,
        "exportXlsx": True,
        "exportPdf": True,
        "importCsv": True,
        "importJson": True,
        "fontSize": 12,
        "rowHeight": 25,
        "fitToWidth": True,
        "paginationEnabled": False,
        "paginationRows": 10,
        "staticCreate": True,
        "staticUpdate": True,
        "staticDelete": True,
        "paginationPosition": "up",
        "source": "dflt.rivers",
        "crudFields": [
            {
                "crudName": f"{tool_name}",
                "fieldName": "dflt.rivers.id",
                "enabled": True,
                "position": 0,
                "h": 3,
                "i": "dflt.rivers.id",
                "w": 1,
                "x": 0,
                "y": 0
            },
            {
                "crudName": f"{tool_name}",
                "fieldName": "dflt.rivers.name",
                "enabled": True,
                "position": 1,
                "h": 3,
                "i": "dflt.rivers.name",
                "w": 1,
                "x": 0,
                "y": 3
            },
            # {
            #     "crudName": f"{tool_name}",
            #     "fieldName": "dflt.rivers.length",
            #     "enabled": False,
            #     "position": 2,
            #     "h": 2,
            #     "i": "dflt.rivers.length",
            #     "w": 1,
            #     "x": 0,
            #     "y": 4
            # },
            {
                "crudName": f"{tool_name}",
                "fieldName": "dflt.rivers.flow_rate",
                "enabled": True,
                "position": 4,
                "h": 3,
                "i": "dflt.rivers.flow_rate",
                "w": 1,
                "x": 0,
                "y": 6
            }
        ]
      }
    }


    base_url_api = os.getenv('BASE_URL_API')
    resp_post_tool = requests.post(base_url_api + '/tools',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=post_request_body)
    requests.patch(base_url_api + f'/tools/{tool_name}',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=patch_request_body)
    
    params = {
      "pks[id]": 12321,
      "pks[name]": "Каменка"
      }

    yield resp_post_tool

    base_url_api = os.getenv('BASE_URL_API')
    requests.delete(base_url_api + f'/tools/{tool_name}/crud',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  params=params)
    requests.delete(base_url_api + f'/tools/{tool_name}',
                  headers={"Authorization": f"Bearer {get_access_token_admin}"},
                  json=post_request_body)

    return resp_post_tool
