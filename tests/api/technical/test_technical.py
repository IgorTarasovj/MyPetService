import pytest
from http import HTTPStatus
from src.clients.http_builder import get_http_client
from src.tools.assertions.common import assert_status_code, validate_response
from src.models.technical.technical import GetResponseStatusSchema



def test_status():
    api_client = get_http_client()
    response = api_client.get(url="/status")

    assert_status_code(response.status_code, HTTPStatus.OK)
    validate_response(response.json(), GetResponseStatusSchema)
