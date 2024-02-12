from unittest.mock import patch
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.drivers.barcode_handler import BarcodeHandler

@patch.object(BarcodeHandler, "create_barcode")
def test_validate_and_create(mock_create_barcode):
    mock_create_barcode.return_value = "tags/1234"
    request = HttpRequest(body={"product_code": "1234"})
    tag_creator_view = TagCreatorView()
    response = tag_creator_view.validate_and_create(request)
    assert response.status_code == 200
