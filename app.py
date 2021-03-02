from flask import Flask
from flask_restful import Api

# Flask ApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

# Endpoints
from endpoints.person import PersonItem, PersonByCpf, PersonCollection
from endpoints.address import AddressItem, AddressCollection

from db import config_db

app = Flask(__name__)
api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='RESTful API Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})

docs = FlaskApiSpec(app)

def initialize_app(app):
    config_db(app)

    # Adicionando recursos na API
    api.add_resource(PersonCollection, '/people')
    api.add_resource(PersonItem, '/people/<int:person_id>')
    api.add_resource(PersonByCpf, '/people/cpf/<string:cpf>')

    api.add_resource(AddressCollection, '/addresses')
    api.add_resource(AddressItem, '/addresses/<int:address_id>')

    #  Registrando recursos para exibir no Swagger UI
    docs.register(PersonCollection)
    docs.register(PersonItem)
    docs.register(PersonByCpf)

    docs.register(AddressCollection)
    docs.register(AddressItem)


def main():
    initialize_app(app)
    app.run(debug=True)


if __name__ == '__main__':
    main()
