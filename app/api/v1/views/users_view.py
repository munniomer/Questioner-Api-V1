"""User views contains Signup Resources"""

from app.api.v1.models.users_model import UserModel  
from flask import Flask, request, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash
from app.validators.validators import Validators

db = UserModel()
validate = Validators()

class SignupResource(Resource):
    """Resource for user registration."""

    def post(self):
        """Method for posting user data"""
        data = request.get_json()
        if not data:
            return {"message": "Please provide a json data"}, 400
        if not all(key in data for key in ["username", "email", "password", "confirm_password"]):
            return {"message": "Some fields are missing"}, 400
        print(data)
        username = data["username"]
        email = data["email"]
        password = data["password"]
        confirm_password = data["confirm_password"]
        
        #Checks if username is valid
        if not validate.valid_name(username):
            return {'message': "PLease check if username is empty or less 3 letters or contains numbers"}, 400

        # checks if username exists
        check_email = validate.check_username(username)
        if check_email:
            return {'message': 'That username exists. use a unique username'}, 400

         # Checks if email is valid
        if not validate.valid_email(email):
            return {'message': "Please enter a valid email "}, 400

        # checks if email exists
        check_email = validate.check_email(email)
        if check_email:
            return {'message': 'That email exists. use a unique email'}, 400

        # Checks if passwords are empty or less than 3
        if not validate.valid_password(password):
            return {'message': "Please check if your password is empty or less than 3"}, 400

        # checks if confirm password is equal to password
        if confirm_password != password:
            return {"message": "confirm password does not match password"}, 400

        hashpassword = generate_password_hash(password)

        data = db.add_user(username, email, hashpassword)

        return {"message": "User successfully created", }, 201
