from flask_restful import Resource, reqparse
from models.accessPassword import AccessPasswordModel


class AccessPasswords(Resource):

    def get(self):
        return {'AccessPasswords': [accessPassword.json() for accessPassword in AccessPasswordModel.query.all()]}

class AccessPassword(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('customer', type=str)
    arguments.add_argument('portal', type=str)
    arguments.add_argument('user', type=str)
    arguments.add_argument('password', type=str)

    def get(self, id):
        accessPassword = AccessPasswordModel.find_accessPassword(id)
        if accessPassword:
            return accessPassword.json()
        return {'message': 'Access Password not found.'}, 404

    def post(self, id):
        if AccessPasswordModel.find_accessPassword(id):
            return {"message": "Access Password id '{}' already exists.".format(id)}, 400
        data = AccessPassword.arguments.parse_args()
        accessPassword = AccessPasswordModel(id, **data)
        try:
            accessPassword.save_accessPassword()
        except:
            return {'message': 'An internal error ocurred trying to save Access Password'}, 500
        return accessPassword.json(), 200

    def put(self, id):
        data = AccessPassword.arguments.parse_args()
        accessPasswords_found = AccessPasswordModel.find_accessPassword(id)
        if accessPasswords_found:
            accessPasswords_found.update_accessPassword(**data)
            accessPasswords_found.save_accessPassword()
            return accessPasswords_found.json(), 200
        accessPassword = AccessPasswordModel(id, **data)
        accessPassword.save_accessPassword()
        return accessPassword.json(), 201

    def delete(self, id):
        accessPassword = AccessPasswordModel.find_accessPassword(id)
        if accessPassword:
            try:
                accessPassword.delete_accessPassword()
            except:
                return {'message': 'An internal error ocurred trying to delete Access Password.'}, 500
            return {'message': 'Access Password deleted.'}
        return {'message': 'Access Password not found.'}, 404
