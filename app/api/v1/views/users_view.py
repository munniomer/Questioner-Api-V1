"""User views contains Signup Resources"""

from app.api.v1.models.users_model import UserModel  
from flask import Flask, request, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash,check_password_hash
from app.validators.validators import Validators
from werkzeug.exceptions import BadRequest,Forbidden,NotFound

db = UserModel()
validate = Validators()

class SignupResource(Resource):
    """Resource for user registration."""

    def post(self):
        """Method for posting user data"""
        data = request.get_json()
        if not data:
            raise BadRequest ("Please provide a json data")
        if not all(key in data for key in ["username", "email", "password", "confirm_password","role"]):
            raise BadRequest ("Some fields are missing")
        print(data)
        username = data["username"]
        email = data["email"]
        password = data["password"]
        confirm_password = data["confirm_password"]
        role = data["role"]
        
        #Checks if username or role is valid
        if not validate.valid_name(username) or not validate.valid_name(role):
            raise BadRequest ("PLease check if username or role is empty or less 3 letters or contains numbers")
        
        # checks if username exists
        check_username = validate.check_username(username)
        if check_username:
            raise Forbidden('That username exists. use a unique username')

        # Checks if email is valid
        if not validate.valid_email(email):
            raise BadRequest ("Please enter a valid email ")

        # checks if email exists
        check_email = validate.check_email(email)
        if check_email:
            raise Forbidden ("That email exists. use a unique email")

        # Checks if passwords are empty or less than 3
        if not validate.valid_password(password):
            raise BadRequest ("Please check if your password is empty or less than 6")

        # checks if confirm password is equal to password
        if confirm_password != password:
            raise BadRequest ("confirm password does not match password")

        hashpassword = generate_password_hash(password)

        data = db.add_user(username, email, hashpassword,role)

        for userdata in data:
            response = { "userId": userdata["userId"],
                        "username": userdata["username"],
                         "role": userdata["role"] }
            
        
        return {"status": 201,
                "message": "User successfully created", 
                "user data": response}, 201

class LoginResource(Resource):
    """Resource for user login """

    def post(self):
        """method for login users"""
        request_data = request.get_json()
        if not request_data:
            return {"message": "Please provide a correct json data"}, 400
        if not all(key in request_data for key in ["email", "password"]):
            return {"message": "Please provide your email and password"}, 400
        print(request_data)
        email = request_data["email"]
        password = request_data["password"]

        # Checks if email is valid
        if not validate.valid_email(email):
            raise BadRequest  ("Please enter a valid email ")

        # checks if email exists
        if not validate.check_email(email):
            raise NotFound ("That email does not exist. Please register first")
        result = validate.check_email(email)
    
        for userdata in result:
            userpass = userdata["password"]
        
        if check_password_hash(userpass, password):
              return {"status": 200,
                     "message": "Successfully loged in"},200
        raise BadRequest ("Password is incorrect")
            
      