"""Validators Module"""
import re
from app.api.v1.models.users_model import users
from app.api.v1.models.meetups_model import MeetupModel,meetups
from werkzeug.exceptions import BadRequest

db = MeetupModel()

class Validators():
    """Validators Class"""

    def check_email(self, email):
        """Method for checking if user email exist"""
        user = [user for user in users if user['email'] == email]
        if user:
            return user
    

    def check_username(self, username):
        """Method for checking if username exist"""
        user = [user for user in users if user['username'] == username]
        if user:
            return True
        return False

    def valid_email(self, email):
        """ valid email """
        regex = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(regex, email)

    def valid_name(self, name):
        """validate username"""
        regex = "^[a-zA-Z]{3,}$"
        return re.match(regex, name)

    def valid_password(self, password):
        """ valid password """
        regex = "^[a-zA-Z0-9@_+-.]{6,}$"
        return re.match(regex, password)
    
    def check_data(self,data):
        """Method for checking if data is provided"""
        if not data:
            raise BadRequest("Please provide a json data")

    def check_signup_data_fileds(self, data):
        """Method for checking if all the signup fields are provided"""
        if not all(key in data for key in ["username", "email", "password", "confirm_password", "role"]):
            raise BadRequest("Some fields are missing")
    
    def check_login_data_fields(self,data):
        """Method for checking if all the login fields are provided"""
        if not all(key in data for key in ["email", "password"]):
             raise BadRequest ("Please provide your email and password")
    
    def validate_meetup_data(self,data):
        """Method for validating meetup data"""
        if not all(key in data for key in ["venue", "title", "happening_on"]):
            raise BadRequest ("Some fields are missing")
        elif data["venue"] == "" or data["title"] == "" or data["happening_on"] == "":
            raise BadRequest("Please fill all the fields")
        elif data["venue"].isdigit() or data["title"].isdigit():
            raise BadRequest("Title and Venue should not be provided in numbers")


     





