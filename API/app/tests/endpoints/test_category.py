from unittest.mock import patch

from main.util.mappers.categorymapper import CategoryMapper
from tests.endpoints.test_base import TestBase


class TestCategoryEndpoint(TestBase):
    def setUp(self):
        super(TestCategoryEndpoint, self).setUp()

    @patch("main.controller.category_controller.DBapi.mcategories.get")
    def test_get_single_category(self, mock_db):
        test_category = {
            "mcategoryid": 1,
            "name": "Distance"
        }
        test_category_mapper = CategoryMapper(**test_category)

        mock_db.return_value = [test_category_mapper]

        response = self.app.get("category/1")
        data = response.json

        assert data == test_category
        mock_db.assert_called_once_with('1')

    @patch("main.controller.category_controller.DBapi.mcategories.get")
    def test_get_category_list(self, mock_db):
        test_category_list = [
            {
                "mcategoryid": 1,
                "name": "Distance"
            },
            {
                "mcategoryid": 2,
                "name": "Weight"
            }
        ]

        test_category_mapper_list = [
            CategoryMapper(**category_dict)
            for category_dict in test_category_list
        ]

        mock_db.return_value = test_category_mapper_list

        response = self.app.get("/category")
        data = response.json

        assert data == {
            "categories": test_category_list
        }
        mock_db.assert_called_once()
