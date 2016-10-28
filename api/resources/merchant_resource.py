from flask import request
from flask_restful import reqparse, marshal_with
# import Merchant database model
from database.model import db, Merchant
from common.utils import email  # used for custom email type and reqparse
from resources.base_resource import BaseResource

# call description on the object

response_to_sql_map = {'id': Merchant.merchant_ID,
                       'merchant': Merchant.merchant_Email,
                       'first_name': Merchant.merchant_Fname,
                       'last_name': Merchant.merchant_Lname,
                       'license': Merchant.merchant_License,
                       'password': Merchant.merchant_Password,
                       'phone': Merchant.merchant_Phone,
                       'paypal_id': Merchant.merchantPayPal_ID
                       }


class MerchantResource(BaseResource):
    def __init__(self):
        super(MerchantResource, self).__init__()
        self.field_map = response_to_sql_map

    def get(self, merchant_id):
        # Get a merchant from the DB
        merchant_info = Merchant.query.get(merchant_ID)
        if merchant_info is None:
            # Could not find that persons id
            # Return HTTP 400 BAD REQUEST and give some error context
            return {'status': 400, 'message': 'merchant_id provided does not exist'}, 400

        # Convert the SQLAlchemy object to a response
        # Also return HTTP 200 OK
        return self.make_response_from_sqlalchemy(merchant_info), 200

    def put(self, merchant_id):
        # Updates a Merchant in the db
        merchant_info = Merchant.query.get(merchant_ID)
        if merchant_info is None:
            # Could not find that persons id
            # Return HTTP 400 BAD REQUEST and give some error context
            return {'status': 400, 'message': 'merchant_id provided does not exist'}, 400

        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('email', type=email)
        parser.add_argument('phone', type=str)
        parser.add_argument('paypal_id', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('license', type=str)
        # now actually do the parsing
        # strict will throw an error and return a response if something like invalid email or a unrecognized param
        args = parser.parse_args(strict=True)
        merchant_info = self.update_sqlachemy_object(merchant_info, args)
        db.session.commit()  # write the updated Merchant object to the database
        return self.make_response_from_sqlalchemy(merchant_info), 202  # HTTP 202 ACCEPTED

    def post(self):
        # Creates a Merchant in the db. Do not pass in a merchant_id, the DB created this!
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('email', type=email, required=True)
        parser.add_argument('phone', type=str, required=True)
        parser.add_argument('paypal_id', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('license', type=str, required=True)
        args = parser.parse_args(strict=True)
        new_merchant = self.update_sqlachemy_object(Merchant(), args)
        db.session.add(new_merchant)
        db.session.commit()
        return self.make_response_from_sqlalchemy(new_merchant), 201  # HTTP 201 CREATED

    def delete(self, merchant_id):
        # An example of how to do deletion
        pass
