"""User views contains Question Resources"""

from flask import Flask, request, jsonify
from flask_restful import Resource
from werkzeug.exceptions import BadRequest, NotFound
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
        user_Id = data["user_Id"]
        meetup_Id = data["meetup_Id"]
        title = data["title"]
        body = data["body"]

        if not validate.valid_question(title) or not validate.valid_question(body):
            raise BadRequest(
                "title and body cant be empty or less than 5 words")

        validate.check_user(user_Id)
        validate.check_meetup(meetup_Id)
        validate.check_question(title)

        data = db.add_question(user_Id, meetup_Id, title, body)

        return {"status": 201,
                "message": "Meetup successfully created",
                "meetup data": data}, 201

    def put(self, question_Id):
        """Method for downvoting question vote """
        question = db.downvote_question(question_Id)
        if not question:
            raise BadRequest("Question does not exist")
        return {
            "message": "question downvoted succesfully",
            "Question": question
        },200


class UpvoteResource(Resource):
    def put(self, question_Id):
        """Method for updating question vote """
        question = db.upvote_question(question_Id)
        if not question:
            raise BadRequest("Question does not exist")
        return {
            "message": "question upvoted succesfully",
            "Question": question
        },200
