from flask import Flask
from flask_restful import Resource, Api

from db import config_db

app = Flask(__name__)
api = Api(app)

class MyApi(Resource):
    def get(self):
        return {'message': 'My First Flask RESTful API!'}


api.add_resource(MyApi, '/')


def initialize_app(app):
    config_db(app)


if __name__ == '__main':
    initialize_app(app)
    app.run(debug=True)
