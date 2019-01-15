"""User views contains Signup Resources"""

from flask import Flask, request, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, Forbidden, NotFound
from app.api.v1.models.users_model import UserModel
from app.validators.validators import Validators

db = UserModel()
validate = Validators()


class SignupResource(Resource):
    """Resource for user registration."""

    def post(self):
        """Method for posting user data"""
        data = request.get_json()
        validate.check_data(data)
        validate.check_signup_data_fileds(data)
        print(data)
        username = data["username"]
        email = data["email"]
        password = data["password"]
        confirm_password = data["confirm_password"]
        role = data["role"]

        if not validate.valid_name(username) or not validate.valid_name(role):
            raise BadRequest(
                "PLease check if username or role is empty or less 3 letters or contains numbers")

        check_username = validate.check_username(username)
        if check_username:
            raise Forbidden('That username exists. use a unique username')

        if not validate.valid_email(email):
            raise BadRequest("Please enter a valid email ")

        check_email = validate.check_email(email)
        if check_email:
            raise Forbidden("That email exists. use a unique email")

        if not validate.valid_password(password):
            raise BadRequest(
                "Please check if your password is empty or less than 6")

        if confirm_password != password:
            raise BadRequest("confirm password does not match password")

        hashpassword = generate_password_hash(password)

        data = db.add_user(username, email, hashpassword, role)

        for userdata in data:
            response = {"userId": userdata["userId"],
                        "username": userdata["username"],
                        "role": userdata["role"]}

        return {"status": 201,
                "message": "User successfully created",
                "user data": response}, 201


class LoginResource(Resource):
    """Resource for user login """

    def post(self):
        """method for login users"""
        request_data = request.get_json()
        validate.check_data(request_data)
        validate.check_login_data_fields(request_data)
        print(request_data)
        email = request_data["email"]
        password = request_data["password"]

        if not validate.valid_email(email):
            raise BadRequest("Please enter a valid email ")

        if not validate.check_email(email):
            raise NotFound("That email does not exist. Please register first")
        result = validate.check_email(email)

        for userdata in result:
            userpass = userdata["password"]

        if check_password_hash(userpass, password):
            return {"status": 200,
                    "message": "Successfully loged in"}, 200
        raise BadRequest("Password is incorrect")
