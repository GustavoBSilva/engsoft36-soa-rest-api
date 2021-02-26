from marshmallow import Schema, fields


class StateSchema(Schema):
    id = fields.Integer()
    acronym = fields.String()
    name = fields.String()