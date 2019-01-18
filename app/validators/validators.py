"""Validators Module"""
import re
import datetime
from werkzeug.exceptions import BadRequest, NotFound
from app.api.v1.models.users_model import users
from app.api.v1.models.meetups_model import MeetupModel, meetups
from app.api.v1.models.questions_model import questions
from app.api.v1.models.rsvps_model import rsvps


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

    def check_data(self, data):
        """Method for checking if data is provided"""
        if not data:
            raise BadRequest("Please provide a json data")

    def check_signup_data_fileds(self, data):
        """Method for checking if all the signup fields are provided"""
        if not all(key in data for key in ["username", "email", "password", "confirm_password", "role"]):
            raise BadRequest("Some fields are missing")

    def check_login_data_fields(self, data):
        """Method for checking if all the login fields are provided"""
        if not all(key in data for key in ["email", "password"]):
            raise BadRequest("Please provide your email and password")

    def validate_meetup_data(self, data):
        """Method for validating meetup data"""
        if not all(key in data for key in ["venue", "title", "happening_on"]):
            raise BadRequest("Some fields are missing")
        elif data["venue"].isdigit() or data["title"].isdigit():
            raise BadRequest(
                "Title and Venue should not be provided in numbers")
        elif data["venue"] == "" or  data["title"] == "" or  data["happening_on"] == "" or  data["title"].isspace() or data["venue"].isspace() or data["happening_on"].isspace():
            raise BadRequest("please fill all the fields")

    def validate_question_data(self, data):
        if not all(key in data for key in ["user_Id", "meetup_Id", "title", "body"]):
            raise BadRequest("Some fields are missing")
        elif isinstance(data["title"], int):
            raise BadRequest(
                "title and body should not be provided in numbers")
        elif data["title"].isdigit() or data["body"].isdigit():
            raise BadRequest("title and body cant contain only numbers")
        elif data["title"] == "" or  data["body"] == "" or data["title"].isspace() or data["body"].isspace():
            raise BadRequest("title or body should not be empty")

    def check_user(self, userId):
        """Method for checking if user exist"""
        user = [user for user in users if user['userId'] == userId]
        if not user:
            raise NotFound('That user doesnt exist, plz create a user')

    def check_meetup(self, meetup_Id):
        """Method for checking if meetup exists"""
        meetup = db.get_specific_meetup(meetup_Id)
        if not meetup:
            raise NotFound('That meetup doesnt exist.')

    def check_question(self, title):
        """Method for checking if meetup exists"""
        question = [
            question for question in questions if question['title'] == title]
        if question:
            raise BadRequest("There is a question title similar that exists")

    def valid_question(self, question):
        """validate question"""
        regex = "^[a-zA-Z0-9]{5,}$"
        return re.match(regex, question)

    def check_rsvps(self, user_Id):
        """Method for checking if user already responded"""
        user = [user for user in rsvps if user['user_Id'] == user_Id]
        if user:
            return user

    def validate_rsvps(self, data):
        if not all(key in data for key in ["user_Id", "response"]):
            raise BadRequest("Some fields are missing")
        elif isinstance(str.strip(data["response"]), int) or str.strip(data["response"]).isdigit():
            raise BadRequest(
                "response should not be provided in numbers")
        elif data["response"] == "" or data["response"].isspace():
            raise BadRequest("response should not be empty")
    
    def valid_date(self, happeningdate):
        """Method for validating date"""
        createdOn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        if happeningdate < createdOn:
            raise BadRequest ("Meetup cant happen in the past")
       


