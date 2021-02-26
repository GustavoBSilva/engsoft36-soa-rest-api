from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class MyApi(Resource):
    def get(self):
        return { 'message': 'My First Flask RESTful API!'}

api.add_resource(MyApi, '/')

if __name__ == '__main':
    app.run(debug=True)
