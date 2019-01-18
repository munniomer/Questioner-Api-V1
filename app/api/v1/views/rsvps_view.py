"""Rsvps views contains Rsvps Resources"""

from flask import Flask, request, jsonify,json
from flask_restful import Resource
from werkzeug.exceptions import BadRequest,NotFound
from app.validators.validators import Validators
from app.api.v1.models.rsvps_model import RsvpsModel, rsvps

db = RsvpsModel()
validate = Validators()

class RsvpsResource(Resource):
    """Resource for Rsvps Meetups."""

    def post(self,meetup_Id):
        """Method for Rsvps"""
        data = request.get_json()
        validate.check_data(data)
        validate.validate_rsvps(data)
        print(data)
       
        user_Id = data["user_Id"]
        meetup_Id = meetup_Id
        response = data["response"] 

        

        validate.check_user(user_Id)
        validate.check_meetup(meetup_Id)
        users = validate.check_rsvps(user_Id)
        if users:
           for user in users:
               meetupId = user["meetup_Id"]
           if meetupId == meetup_Id:
               raise BadRequest("you already responded in that meeting")       

        data = db.add_rsvps(user_Id,meetup_Id,str.strip(response))

        return {"status": 201,
                "message": "Rsvps successfully created",
                "Rsvp data": data}, 201
    
 
