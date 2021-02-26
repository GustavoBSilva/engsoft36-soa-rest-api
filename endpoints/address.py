from flask_apispec import use_kwargs, marshal_with, doc
from flask_apispec.views import MethodResource

from flask_restful import Resource, abort, reqparse
from business.address import AddressDao

from schemas.address import AddressSchema

from webargs import fields

post_parser = reqparse.RequestParser()
post_parser.add_argument('zip_code', dest='zip_code', type=str, required=True, help='Postal Code field')
post_parser.add_argument('street', dest='street', type=str, required=True, help='Street field')
post_parser.add_argument('number', dest='number', type=str, required=True, help='Number field')
post_parser.add_argument('additional', dest='additional', type=str, required=False, help='Additional information field')


class AddressItem(MethodResource, Resource):
    @doc(description='Get an address by ID.', tags=['Address'])
    @marshal_with(AddressSchema)
    def get(self, address_id):
        address = AddressDao.get_by_id(self, address_id)

        if address is None:
            abort(404, message="Address Not Found")

        return address.to_dict()

    @doc(description='Edit an address.', tags=['Address'])
    @marshal_with(AddressSchema)
    def put(self, address_id):
        pass

    @doc(description='Delete an address.', tags=['Address'])
    @marshal_with(None, code=204)
    def delete(self, address_id):
        pass


class AddressCollection(MethodResource, Resource):
    @doc(description='Get all addresses.', tags=['Address'])
    @marshal_with(AddressSchema(many=True))
    def get(self):
        addresses = AddressDao.get_all(self)

        return [address.to_dict() for address in addresses]

    @doc(description='Add a new address.', tags=['Address'])
    @marshal_with(AddressSchema, code=201)
    def post(self):
        args = post_parser.parse_args()

        new_address = AddressDao.add_address(self, args.zip_code, args.street, args.number, args.additional)

        return new_address.to_dict()
