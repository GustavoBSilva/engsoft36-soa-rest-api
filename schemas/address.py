from marshmallow import Schema, fields

from schemas.city import CitySchema
from schemas.state import StateSchema
from schemas.country import CountrySchema


class AddressSchema(Schema):
    id = fields.Integer()
    zip_code = fields.String(required=True)
    street = fields.String(required=True)
    number = fields.Integer(required=True)
    additional = fields.String(required=False)
    city = fields.Nested(CitySchema)
    state = fields.Nested(StateSchema)
    country = fields.Nested(CountrySchema)
