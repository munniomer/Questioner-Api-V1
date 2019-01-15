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
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.new_user1 = {
            "username": "  ",
            "email": "munniomer@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.new_user2 = {
            "username": "Muniraa",
            "email": "munii",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.new_user3 = {
            "username": "muni",
            "email": "munni@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.new_user4 = {
            "username": "munir",
            "email": "munni@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
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
            "password": "m12m12",
            "confirm_password": "m",
            "role": "user"
        }

        self.new_user7 = {
            "username": "Fatma",
            "email": "Fatma@gmail.com",
            "password": "m12m12",
            "role": "user"

        }


        self.new_user9 = {
            
            "email": "shidaneail.com",
            "password": "m12m12"
            
           
        }

        self.new_user10 = {
            "email": "shidane1@gmail.com"
            
           
        }

        self.new_user11 = {
            "username": "Mom",
            "email": "Mom@gmail.com",
            "password": "m12m12",
            "role": "user"

        }


        self.new_user12 = {
            "username": "Mum",
            "email": "Mumm@gmail.com",
            "password": "m12m12",
            "role": "user"

        }


        self.new_user13 = {
            
            "email": "Mumm@gmail.com",
            "password": "m12m12"
            

        }
        self.meetup = {
        "venue": "iHub Kenya",
        "title": "Python Meetup",
        "happening_on": "1/25/2019"
    }

        self.meetup1 = {
        "venue": "iHub Kenya",
        "happening_on": "1/25/2019"
    }
        


    def tearDown(self):
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None

    if __name__ == '__main__':
        unittest.main(verbosity=2)