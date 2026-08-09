import allure
from http import HTTPStatus
from src.clients.http_builder import get_http_client
from src.schemas.users.user import GerUserResponseSchema
from src.tools.assertions.common import assert_status_code, validate_response


@allure.title("Get default user")
def test_user(users_repository):
    api_client = get_http_client()
    user_id = users_repository.get_default_user_id()
    response = api_client.get(params= {'user_id':str(user_id)}, url="/users/user")
    assert_status_code(response.status_code, HTTPStatus.OK)
    validate_response(response.json(), GerUserResponseSchema)