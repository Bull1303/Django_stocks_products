from rest_framework.test import APIClient


class TestSmth(APIClient):
    def test_sample_view_ok(self):
        client = APIClient()
        url = '/api/v1/test/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
