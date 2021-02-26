from marshmallow import Schema, fields

from schemas.address import AddressSchema


class PersonSchema(Schema):
    class Meta:
        fields = ('name', 'cpf', 'birth_date')


class PersonResponseSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    cpf = fields.String(required=True)
    birth_date = fields.String(required=True)
    address = fields.Nested(AddressSchema)


class PersonRequestSchema(Schema):
    name = fields.String(required=True)
    cpf = fields.String(required=True)
    birth_date = fields.String(required=True)
