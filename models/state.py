from db import db

from sqlalchemy_serializer import SerializerMixin


class State(db.Model, SerializerMixin):
    __tablename__ = 'state'

    id = db.Column(db.Integer, primary_key=True)
    acronym = db.Column(db.String(2), nullable=False)  # Sigla
    name = db.Column(db.String(500), nullable=False)  # Nome