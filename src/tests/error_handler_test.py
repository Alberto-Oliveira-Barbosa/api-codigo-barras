from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.error_handler import handle_errors

def test_handle_errors_with_http_unprocessable_entity_error():
    error = HttpUnprocessableEntityError("Error Test")
    response = handle_errors(error)

    assert "title" in response.body
    assert "details" in response.body

def test_handle_errors_with_generic_exception():
    error = Exception("Error Test")
    response = handle_errors(error)

    assert response.status_code == 500
    assert "title" in response.body
    assert "details" in response.body
