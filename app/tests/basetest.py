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

        self.new_user14 = {
            "username": "siman",
            "email": "siman@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.new_user15 = {
            "email": "siman@gmail.com",
            "password": "m12m12"
        }

        self.new_user16 = {
            "username": "susan",
            "email": "susan@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.new_user17 = {
            "email": "susan@gmail.com",
            "password": "m78m78"
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

        self.meetup2 = {
            "venue": "",
            "title": "Python Meetup",
            "happening_on": "1/25/2019"
        }

        self.meetup3 = {
            "venue": "7888",
            "title": "Python Meetup",
            "happening_on": "1/25/2019"
        }

        self.question = {
            "user_Id": 1,
            "meetup_Id": 1
        }

        self.question1 = {
            "user_Id": 1,
            "meetup_Id": 1,
            "title": "ques11",
            "body": "python"
        }

        self.new_user18 = {
            "username": "zamzam",
            "email": "zamzam@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.question2 = {
            "user_Id": 1,
            "meetup_Id": 1,
            "title": "",
            "body": "python"
        }

        self.new_user19 = {
            "username": "Asma",
            "email": "Asma@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.question3 = {
            "user_Id": 1,
            "meetup_Id": 1,
            "title": 9999,
            "body": "python"
        }

        self.question4 = {
            "user_Id": 1,
            "meetup_Id": 1,
            "title": "9999",
            "body": "python"
        }

        self.question5 = {
            "user_Id": 1,
            "meetup_Id": 1,
            "title": "Muuun",
            "body": "python"
        }

        self.question6 = {
            "user_Id": 1,
            "meetup_Id": 1,
            "title": "Heyyys",
            "body": "python"
        }
        self.rsvp = {
            "user_Id":  1
        }

        self.rsvp1 = {
            "user_Id": 1,
            "response": "  YES  "
        }
        self.new_user19 = {
            "username": "maria",
            "email": "maria@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.rsvp2 = {
            "user_Id": 6,
            "response": "  YES  "
        }

        self.rsvp3 = {
            "user_Id": 1,
            "response": "  YES  "
        }

        self.rsvp4 = {
            "user_Id": 1,
            "response": "882"
        }

        self.rsvp5 = {
            "user_Id": 1,
            "response": " "
        }

        self.question10 = {
            "user_Id": 1,
            "meetup_Id": 1,
            "title": "english",
            "body": "python"
        }

        self.new_user20 = {
            "username": "Asmaa",
            "email": "asmaa@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.question11 = {
            "user_Id": 1,
            "meetup_Id": 1,
            "title": "Javascript",
            "body": "python"
        }

        self.new_user21 = {
            "username": "Abdalla",
            "email": "Abdalla@gmail.com",
            "password": "m12m12",
            "confirm_password": "m12m12",
            "role": "user"
        }

        self.question14 = {
            "user_Id": 1,
            "meetup_Id": 2,
            "title": "ques11",
            "body": "python"
        }

    def tearDown(self):
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None

    if __name__ == '__main__':
        unittest.main(verbosity=2)
