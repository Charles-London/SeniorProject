# A base resource with custom functionality
from flask_restful import Resource


class BaseResource(Resource):
    def __init__(self):
        self.field_map = {}
        super(BaseResource, self).__init__()

    def update_sqlachemy_object(self, sqlalchemy_obj, parser_args):
        """Updates and returns a SQLAlchemy Object given arguments from the parser
           This is for PUT operations
           After running this method, call db.session.commit() to write to the database
           It converts arguments from the parser (which come from the API data) to SQL field names by using
           the field_map
        """
        parser_args = dict(parser_args)
        for response_field, sql_field in self.field_map.iteritems():
            if parser_args.get(response_field, None) is not None:  # ensure field is present and not None
                setattr(sqlalchemy_obj, sql_field.description, parser_args[response_field])
        return sqlalchemy_obj

    def make_response_from_sqlalchemy(self, sqlalchemy_obj):
        """Given a sqlalchemy_object as the result of a Model.query.get() operation, returns a JSON
           response. It converts the SQL field names to a JSON response by using the field_map.
           """
        response = {}
        for response_field, sql_field in self.field_map.iteritems():
            response[response_field] = getattr(sqlalchemy_obj, sql_field.description)
        return response
