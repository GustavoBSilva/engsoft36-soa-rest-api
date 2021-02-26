from db import db

from sqlalchemy_serializer import SerializerMixin

from models.address import Address


class Person(db.Model, SerializerMixin):
    __tablename__ = 'person'

    serialize_only = ('id', 'name', 'cpf', 'birth_date', 'address')
    serialize_rules = ('-address.person',)

    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    name = db.Column(db.String(200), nullable=False)  # com nullable sendo 'false' a coluna não pode ficar vazia
    cpf = db.Column(db.String(12), nullable=True)
    birth_date = db.Column(db.String(10), nullable=True)

    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)

    address = db.relationship(Address, backref="person")

    def __init__(self, name, cpf, birth_date):
        self.name = name
        self.cpf = cpf
        self.birth_date = birth_date

    def __repr__(self):
        return '<Person %r>' % self.name
