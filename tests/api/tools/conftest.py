import pytest
import requests


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
