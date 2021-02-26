from models.address import Address
from db import db


class AddressDao(object):
    def get_all(self):
        return Address.query.all()

    def get_by_id(self, _id):
        return Address.query.filter_by(id=_id).first()

    def get_by_zip_code(self, _zip_code):
        return Address.query.filter_by(zip_code=_zip_code).first()

    def add_address(self, _zip_code, _street, _number, _additional):
        new_model = Address(zip_code=_zip_code, street=_street, number=_number, additional=_additional)

        db.session.add(new_model)  # add new model to database session
        db.session.commit()  # commit changes to session

        return new_model

    def update_address(self, _id, _zip_code, _street, _number, _additional):
        model_to_update = Address.query.filter_by(id=_id).first()

        model_to_update.zip_code = _zip_code
        model_to_update.street = _street
        model_to_update.number = _number
        model_to_update.additional = _additional

        db.session.commit()

    def delete_address(_id):
        Address.query.filter_by(id=_id).delete()

        db.session.commit()