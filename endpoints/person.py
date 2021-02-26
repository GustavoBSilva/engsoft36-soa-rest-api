from flask_apispec import use_kwargs, marshal_with, doc
from flask_apispec.views import MethodResource

from flask import Response
from flask_restful import Resource, abort, reqparse

from business.person import PersonDao

from schemas.person import PersonRequestSchema, PersonResponseSchema, PersonSchema

from webargs import fields


class PersonItem(MethodResource, Resource):
    @doc(description='Get a person by ID.', tags=['Person'])
    @marshal_with(PersonSchema)
    def get(self, person_id):
        person = PersonDao.get_by_id(self, person_id)

        if person is None:
            abort(404, message="Person not found")

        return person

    @doc(description='Edit some data from a person.', tags=['Person'])
    @use_kwargs(PersonSchema)
    @marshal_with(PersonSchema)
    def put(self, person_id, **kwargs):
        updated_person = PersonDao.update_person(self, person_id, **kwargs)

        return updated_person

    @doc(description='Delete a person.', tags=['Person'])
    @marshal_with(None, code=204)
    def delete(self, person_id):
        pass


class PersonByCpf(MethodResource, Resource):
    @doc(description='', tags=['Person'])
    @marshal_with(PersonSchema)
    def get(self, cpf):
        person = PersonDao.get_by_cpf(self, cpf)

        if person is None:
            abort(404, message="Person Not Found.")

        return person


class PersonCollection(MethodResource, Resource):
    @doc(description='Get all people.', tags=['Person'])
    @marshal_with(PersonResponseSchema(many=True))
    def get(self):
        people = PersonDao.get_all(self)

        return people

    @doc(description='Add a new person.', tags=['Person'])
    @use_kwargs({'name': fields.Str(required=True), 'cpf': fields.Str(required=True), 'birth_date': fields.Str(required=True)})
    @marshal_with(PersonSchema, code=201)
    def post(self, **kwargs):
        new_person = PersonDao.add_person(self, **kwargs)

        if new_person is None:
            return Response(None, 500, mimetype='application/json')

        return Response(None, 201, mimetype='application/json')
