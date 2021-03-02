from models.address import Address
from db import db


class AddressDao(object):
    def get_all(self):
        return Address.query.all()

    def get_by_id(self, address_id):
        return Address.query.filter_by(id=address_id).first()

    def get_by_zip_code(self, zip_code):
        return Address.query.filter_by(zip_code=zip_code).first()

    def add_address(self, **kwargs):
        new_address = Address(**kwargs)

        db.session.add(new_address)  # adiciona o novo modelo na sessão do BD
        db.session.commit()  # realiza o commit das alterações da sessão

        return new_address

    def update_address(self, address_id, zip_code, street, number, additional):
        model_to_update = Address.query.filter_by(id=address_id).first()

        model_to_update.zip_code = zip_code
        model_to_update.street = street
        model_to_update.number = number
        model_to_update.additional = additional

        db.session.commit()

    def delete_address(self, address_id):
        Address.query.filter_by(id=address_id).delete()

        db.session.commit()
