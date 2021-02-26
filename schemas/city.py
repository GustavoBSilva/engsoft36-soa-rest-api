from marshmallow import Schema, fields


class CitySchema(Schema):
    id = fields.Integer()
    acronym = fields.String()
    name = fields.String()