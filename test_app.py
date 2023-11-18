import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def test_hello_world(self):
        # Send a GET request to the '/' route
        response = self.app.get('/')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response data contains the expected message
        self.assertIn(b'Hello, World!', response.data)

if __name__ == '__main__':
    unittest.main()
