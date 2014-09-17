from tests.utils import NDBTestCase


class TestAPI(NDBTestCase):

    def test_get_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
