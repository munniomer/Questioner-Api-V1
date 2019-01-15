"""Validators Module"""
import re
from app.api.v1.models.users_model import users


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