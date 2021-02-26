from db import db

from sqlalchemy_serializer import SerializerMixin

from models.city import City
from models.state import State
from models.country import Country


class Address(db.Model, SerializerMixin):
    __tablename__ = 'address'

    serialize_only = ('id', 'zip_code', 'street', 'number', 'additional', 'country')
    serialize_rules = ('-city.address', '-state.address', '-country.address',)

    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.String(50), nullable=False)  # CEP
    street = db.Column(db.String(200), nullable=False)  # Logradouro
    number = db.Column(db.Integer, nullable=False)  # Número
    additional = db.Column(db.String(500), nullable=True)  # Complemento

    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)  # Cidade
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=True)  # Estado
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)  # País

    city = db.relationship(City, backref="address")
    state = db.relationship(State, backref="address")
    country = db.relationship(Country, backref="address")

    def __init__(self, zip_code, street, number, additional):
        self.zip_code = zip_code
        self.street = street
        self.number = number
        self.additional = additional

    def __repr__(self):
        return '<Address %r>' % self.street

