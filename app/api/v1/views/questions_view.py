"""User views contains Question Resources"""

from flask import Flask, request, jsonify
from flask_restful import Resource
from werkzeug.exceptions import BadRequest,NotFound
from app.validators.validators import Validators
from app.api.v1.models.questions_model import QuestionsModel


db = QuestionsModel()
validate = Validators()


class QuestionResource(Resource):
    """Resource for Creating Meetups."""

    def post(self):
        """Method for posting meetup data"""
        data = request.get_json()
        validate.check_data(data)
        validate.validate_question_data(data)
        print(data)
        userId = data["userId"]
        meetup_Id = data["meetup_Id"]
        title = data["title"]
        body = data["body"]

        if not validate.valid_question(title) or not validate.valid_question(body):
             raise BadRequest ("title and body cant be empty or less than 5 words")

        validate.check_user(userId)
        validate.check_meetup(meetup_Id)
        validate.check_question(title)
        
      
      

        data = db.add_question(userId, meetup_Id, title, body)

        for questiondata in data:
            response = {"meetup_Id": questiondata["question_Id"],
                        "created_on": questiondata["created_on"],
                        "title": questiondata["title"],
                        "body": questiondata["body"]}

        return {"status": 201,
                "message": "Meetup successfully created",
                "meetup data": response}, 201

