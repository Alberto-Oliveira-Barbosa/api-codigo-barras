from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def test_class():
    error = HttpUnprocessableEntityError("Error Test")
    assert error.name == "UnprocessableEntity"
    assert error.status_code == 422
