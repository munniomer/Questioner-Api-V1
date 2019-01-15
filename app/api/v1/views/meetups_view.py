"""User views contains Signup Resources"""

from app.api.v1.models.meetups_model import MeetupModel
from flask import Flask, request, jsonify
from flask_restful import Resource
from werkzeug.exceptions import BadRequest,NotFound,Forbidden
from app.validators.validators import Validators

db = MeetupModel()
validate = Validators()

class MeetupResource(Resource):
    """Resource for Creating Meetups."""

    def post(self):
        """Method for posting meetup data"""
        data = request.get_json()
        validate.check_data(data)
        validate.validate_meetup_data(data)
        print(data)
        venue = data["venue"]
        title = data["title"]
        happening_on = data["happening_on"]
       
        data = db.add_meetup(venue, title,happening_on)
            
        for meetupdata in data:
            response = { "meetup_Id": meetupdata["meetup_Id"],
                        "created_on": meetupdata["created_on"] }
        
        return {"status": 201,
                "message": "Meetup successfully created", 
                "meetup data": response}, 201

    def get(self):
        """Method for fetching all Meetup records"""
        meetups = db.get_all_meetups()
        if len(meetups) == 0:
            raise NotFound ("There are no meetups created")
        return {'All meetups orders': meetups}, 200

    
class MeetupSpecific(Resource):
    """ class for specific Meetup """

    def get(self, meetup_Id):
        """getting a meetups record by the ID"""
        meetup = db.get_specific_meetup(meetup_Id)
        if meetup:
            return {'meetups details': meetup[0]}, 200
        raise NotFound ("meetups details not found")

