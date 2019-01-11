"""BaseTest modele"""
import unittest
import json
from app import create_app


class BaseTest(unittest.TestCase):
    """This is the test client"""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.new_user = {
            "username": "Munira",
            "email": "munniomer@gmail.com",
            "password": "m123",
            "confirm_password": "m123",
            "role": "user"
        }

        self.new_user1 = {
            "username": "  ",
            "email": "munniomer@gmail.com",
            "password": "m123",
            "confirm_password": "m123",
            "role": "user"
        }

        self.new_user2 = {
            "username": "Muniraa",
            "email": "munii",
            "password": "m123",
            "confirm_password": "m123",
            "role": "user"
        }

        self.new_user3 = {
            "username": "muni",
            "email": "munni@gmail.com",
            "password": "m123",
            "confirm_password": "m123",
            "role": "user"
        }

        self.new_user4 = {
            "username": "munir",
            "email": "munni@gmail.com",
            "password": "m123",
            "confirm_password": "m123",
            "role": "user"
        }

        self.new_user5 = {
            "username": "asha",
            "email": "asha@gmail.com",
            "password": " ",
            "confirm_password": "m",
            "role": "user"
        }

        self.new_user6 = {
            "username": "asha",
            "email": "asha@gmail.com",
            "password": "m123",
            "confirm_password": "m",
            "role": "user"
        }

        self.new_user7 = {
            "username": "Fatma",
            "email": "Fatma@gmail.com",
            "password": "m123",
            "role": "user"

        }

    def tearDown(self):
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None

    if __name__ == '__main__':
        unittest.main(verbosity=2)