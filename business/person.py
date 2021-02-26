from models.person import Person
from db import db


class PersonDao(object):
    def get_all(self):
        return Person.query.all()

    def get_by_id(self, _id):
        return Person.query.filter_by(id=_id).first()

    def get_by_cpf(self, _cpf):
        return Person.query.filter_by(cpf=_cpf).first()

    def add_person(self, **kwargs):
        new_person = Person(**kwargs)

        db.session.add(new_person)  # add new model to database session
        db.session.commit()  # commit changes to database session

        return new_person

    def update_person(self, person_id, name, cpf, birth_date):
        person_to_update = Person.query.filter_by(id=person_id).first()

        if person_to_update is not None:
            person_to_update.name = name
            person_to_update.cpf = cpf
            person_to_update.birth_date = birth_date

            db.session.commit()

        return person_to_update

    def delete_person(self, _id):
        Person.query.filter_by(id=_id).delete()

        db.session.commit()