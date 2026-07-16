from typing import Any

from pydantic import BaseModel, ValidationError


def assert_status_code(actual: int, expected: int):
    """
    Проверяет что ожидаемый статус код соответствует полученному

    :param actual: полученный статус код
    :param expected: ожидаемый статус код
    :raises AssertionError: если статусы отличаются
    """
    assert actual == expected, (
        f'Incorrect status code: {actual}, expected: {expected}'
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param actual: Фактическое значение
    :param expected: ожидаемое значение
    :param name: имя проверяемого поля
    :raises AssertionError: если значения отличаются
    """
    assert actual == expected, (
        f'Incorrect value "{name}": {actual}, expected: {expected}'
    )

def assert_model(actual: BaseModel, expected: BaseModel):
    """
    Строгое сравнение двух pydantic-моделей по каждому полю
    :param actual: фактическая pydantic-модель
    :param expected: Ожидаемая pydantic-модель
    :raises AssertionError: Если хотя бы одно поле отличается
    """
    expected_data = expected.model_dump()

    for attribute_name, value in expected_data.items():
        actual_value = getattr(actual, attribute_name)
        assert_equal(actual_value, value, attribute_name)

def validate_response(response: dict, model: BaseModel):
    try:
        model.model_validate(response)
    except ValidationError as err:
        raise AssertionError(
            f"Response does not match model: \n{err.message}"
        )