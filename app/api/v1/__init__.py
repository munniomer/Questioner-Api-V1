from flask import Flask, Blueprint
from flask_restful import Api, Resource
from app.api.v1.views.users_view import SignupResource, LoginResource
from app.api.v1.views.meetups_view import MeetupResource, MeetupSpecific
from app.api.v1.views.questions_view import QuestionResource,UpvoteResource
from app.api.v1.views.rsvps_view import RsvpsResource


v1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
app = Api(v1)

# Resources are the spiecific route we need to pass the endpoint

# Users
app.add_resource(SignupResource, '/user/register')
app.add_resource(LoginResource, '/user/login')

# Meetups
app.add_resource(MeetupResource, '/meetups', '/meetups/upcoming')
app.add_resource(MeetupSpecific, '/meetups/<int:meetup_Id>')

#Questions
app.add_resource(QuestionResource, '/questions','/questions/<int:question_Id>/downvote')
app.add_resource(UpvoteResource, '/questions/<int:question_Id>/upvote')

# Rsvps
app.add_resource(RsvpsResource, '/meetups/<int:meetup_Id>/rsvps')
