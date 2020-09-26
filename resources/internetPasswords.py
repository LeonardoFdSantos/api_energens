from flask_restful import Resource, reqparse
from models.internetPasswords import InternetPasswordsModel


class InternetPasswords(Resource):

    def get(self):
        return {
            'Internet Password': [internetPassword.json() for internetPassword in InternetPasswordsModel.query.all()]
        }


class InternetPassword(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('customer', type=str)
    arguments.add_argument('ssid', type=str)
    arguments.add_argument('password', type=str)

    def get(self, id):
        internetPassword = InternetPasswordsModel.find_internetPassword(id)
        if internetPassword:
            return internetPassword.json()
        return {'message': 'Internet Password not found.'}, 404

    def post(self, id):
        if InternetPasswordsModel.find_internetPassword(id):
            return {"message": "Internet Password id '{}' already exists.".format(id)}, 400
        data = InternetPassword.arguments.parse_args()
        internetPassword = InternetPasswordsModel(id, **data)
        try:
            internetPassword.save_internetPassword()
        except:
            return {'message': 'An internal error ocurred trying to save Internet Password'}, 500
        return internetPassword.json(), 200

    def put(self, id):
        data = InternetPassword.arguments.parse_args()
        internetPassword_found = InternetPasswordsModel.find_internetPassword(id)
        if internetPassword_found:
            internetPassword_found.update_internetPassword(**data)
            internetPassword_found.save_internetPassword()
            return internetPassword_found.json(), 200
        internetPassword = InternetPassword(id, **data)
        internetPassword.save_internetPassword()
        return internetPassword.json(), 201

    def delete(self, id):
        internetPassword = InternetPasswordsModel.find_internetPassword(id)
        if internetPassword:
            try:
                internetPassword.delete_internetPassword()
            except:
                return {'message': 'An internal error ocurred trying to delete Internet Password.'}, 500
            return {'message': 'Internet Password deleted.'}
        return {'message': 'Internet Password not found.'}, 404
