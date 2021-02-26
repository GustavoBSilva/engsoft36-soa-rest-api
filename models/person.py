from db import db

from sqlalchemy_serializer import SerializerMixin

from models.address import AddressModel


class PersonModel(db.Model, SerializerMixin):
    __tablename__ = 'person'

    serialize_only = ('id', 'name', 'cpf', 'birth_date', 'address')
    serialize_rules = ('-address.person',)

    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    name = db.Column(db.String(200), nullable=False)  # com nullable sendo 'false' a coluna não pode ficar vazia
    cpf = db.Column(db.String(12), nullable=True)
    birth_date = db.Column(db.String(10), nullable=True)

    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)

    address = db.relationship(AddressModel, backref="person")

    def __repr__(self):
        return '<Person %r>' % self.name

    def get_all_people():
        return PersonModel.query.all()

    def get_person_by_id(_id):
        result = PersonModel.query.filter_by(id=_id).first()

        return result

    def get_person_by_cpf(_cpf):
        return PersonModel.query.filter_by(cpf=_cpf).first()

    def add_person(_name, _cpf, _birth_date):
        new_person = PersonModel(name=_name, cpf=_cpf, birth_date=_birth_date)
        db.session.add(new_person)  # add new model to database session
        db.session.commit()  # commit changes to session

        return new_person

    def append_address_to_person(_person_id, _address_id):
        person = PersonModel.query.filter_by(id=_person_id).first()
        founded_address = AddressModel.query.filter_by(id=_address_id).first()

        if person and founded_address:
            founded_address.person.append(person)  # vincular endereço à pessoa
            db.session.commit()  # commit changes to session

    def update_person(_id, _name, _cpf, _birth_date):
        person_to_update = PersonModel.query.filter_by(id=_id).first()

        person_to_update.name = _name
        person_to_update.cpf = _cpf
        person_to_update.birth_date = _birth_date

        db.session.commit()

        return person_to_update

    def delete_person(_id):
        PersonModel.query.filter_by(id=_id).delete()

        db.session.commit()


db.create_all()
