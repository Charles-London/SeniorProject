from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from database.model import db
from resources import user_resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://seniorproject:seniorproject@rwsmith.me/seniorproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # reduce overhead
api = Api(app)
api.add_resource(user_resource.UserResource, '/users/<int:user_id>', '/users/')


@app.route('/', methods=['GET'])
def index():
    return jsonify({'msg': 'This endpoint is not valid, please use another one'})


# Generic 404 handler
@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 404, 'message': '404 NOT FOUND ' + request.url}), 404


@app.errorhandler(500)
def internal_servere_error(error):
    return jsonify({'status': 500, 'message': '500 INTERNAL SERVER ERROR ' + repr(error)})


if __name__ == '__main__':
    db.init_app(app)  # make the database model aware of our application
    app.run(debug=True, threaded=True)  # start the server
