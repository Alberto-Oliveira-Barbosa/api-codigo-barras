from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.validators.tag_creator_validator import tag_creator_validator

class MockJson:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    request = MockJson(json={"product_code": "1234"})
    tag_creator_validator(request=request)

def test_tag_creator_validator_with_error():
    request = MockJson(json={"product_code": 1234})
    try:
        tag_creator_validator(request=request)
        assert False
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)
