from flask import Flask, Blueprint
from flask_restful import Api, Resource 
from app.api.v1.views.users_view import SignupResource


v1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
app = Api(v1)  

#Resources are the spiecific route we need to pass the endpoint

# Users
app.add_resource(SignupResource, '/user/register')

