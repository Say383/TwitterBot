
import unittest
from web_app import app

class FlaskRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Additional tests for other routes

if __name__ == '__main__':
    unittest.main()
