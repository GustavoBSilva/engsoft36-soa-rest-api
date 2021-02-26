from db import db

from sqlalchemy_serializer import SerializerMixin

from models.city import CityModel
from models.state import StateModel
from models.country import CountryModel


class AddressModel(db.Model, SerializerMixin):
    __tablename__ = 'address'

    serialize_only = ('id', 'postal_code', 'street', 'number', 'details', 'country')
    serialize_rules = ('-city.address', '-state.address', '-country.address',)

    id = db.Column(db.Integer, primary_key=True)
    postal_code = db.Column(db.String(50), nullable=False)  # CEP
    street = db.Column(db.String(200), nullable=False)  # Logradouro
    number = db.Column(db.Integer, nullable=False)  # Número
    details = db.Column(db.String(500), nullable=True)  # Complemento

    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)  # Cidade
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=True)  # Estado
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)  # País

    city = db.relationship(CityModel, backref="address")
    state = db.relationship(StateModel, backref="address")
    country = db.relationship(CountryModel, backref="address")

    def get_all_addresses():
        return AddressModel.query.all()

    def get_address_by_id(_id):
        return AddressModel.query.filter_by(id=_id).first()

    def get_address_by_postal_code(_postalCode):
        return AddressModel.query.filter_by(postal_code=_postalCode).first()

    def add_address(_postalCode, _street, _number, _details):
        new_model = AddressModel(postal_code=_postalCode, street=_street, number=_number, details=_details)
        db.session.add(new_model)  # add new model to database session
        db.session.commit()  # commit changes to session

    def update_address(_id, _postalCode, _street, _number, _details):
        model_to_update = AddressModel.query.filter_by(id=_id).first()

        model_to_update.postal_code = _postalCode
        model_to_update.street = _street
        model_to_update.number = _number
        model_to_update.details = _details

        db.session.commit()

    def delete_address(_id):
        AddressModel.query.filter_by(id=_id).delete()

        db.session.commit()


class AddressSchema(ma.SQLAlchemySchema):
    class Meta:
        model = AddressModel


db.create_all()
