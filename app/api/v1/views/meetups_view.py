"""User views contains Signup Resources"""

from app.api.v1.models.meetups_model import MeetupModel
from flask import Flask, request, jsonify
from flask_restful import Resource


db = MeetupModel()

class MeetupResource(Resource):
    """Resource for Creating Meetups."""

    def post(self):
        """Method for posting meetup data"""
        data = request.get_json()
        if not data:
            return {"message": "Please provide a json data"}, 400
        if not all(key in data for key in ["venue", "title", "happening_on"]):
            return {"message": "Some fields are missing"}, 400
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
        # check if the dh is empty
        if len(meetups) == 0:
            return {'message': 'There are no meetups created'}, 404
        return {'All meetups orders': meetups}, 200

