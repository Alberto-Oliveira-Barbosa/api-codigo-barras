from unittest.mock import patch
from src.controllers.tag_creator_controller import TagCreatorController
from src.drivers.barcode_handler import BarcodeHandler

@patch.object(BarcodeHandler, "create_barcode")
def test___create_tag(mock_create_barcode):
    mock_value = "tag_path"
    mock_create_barcode.return_value = f"tags/{mock_value}"
    tag_creator_controller = TagCreatorController()
    result = tag_creator_controller.create(mock_value)
    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "status" in result["data"]
    assert "path" in result["data"]
    assert  result["data"]["type"] == "Tag Image"
    assert  result["data"]["status"] == "Create"
    assert  result["data"]["path"] == f"tags/{mock_value}.png"
