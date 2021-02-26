from marshmallow import Schema, fields


class CountrySchema(Schema):
    id = fields.Integer()
    acronym = fields.String()
    name = fields.String()