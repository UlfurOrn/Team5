
from tests.endpoints.test_base import TestBase


class TestHealthEndpoint(TestBase):
    def setUp(self):
        super(TestHealthEndpoint, self).setUp()

    def test_get_health(self):
        response = self.app.get("/health")
        data = response.json
        assert response.status_code == 200
        assert data == {
            "message": "Healthy"
        }
