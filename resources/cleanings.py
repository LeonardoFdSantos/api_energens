from flask_restful import Resource, reqparse
from models.cleanings import CleaningsModel


class Cleanings(Resource):

    def get(self):
        return {'Cleanings': [cleaning.json() for cleaning in CleaningsModel.query.all()]}

class Cleaning(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('customer', type=str)
    arguments.add_argument('date', type=str)
    arguments.add_argument('nextDate', type=str)
    arguments.add_argument('maximumTime', type=int)

    def get(self, id):
        cleaning = CleaningsModel.find_cleaning(id)
        if cleaning:
            return cleaning.json()
        return {'message': 'cleaning not found.'}, 404

    def post(self, id):
        if CleaningsModel.find_cleaning(id):
            return {"message": "Cleaning id '{}' already exists.".format(id)}, 400
        data = Cleaning.arguments.parse_args()
        cleaning = CleaningsModel(id, **data)
        try:
            cleaning.save_cleaning()
        except:
            return {'message': 'An internal error ocurred trying to save cleaning'}, 500
        return cleaning.json(), 200

    def put(self, id):
        data = Cleaning.arguments.parse_args()
        cleaning_found = CleaningsModel.find_cleaning(id)
        if cleaning_found:
            cleaning_found.update_cleaning(**data)
            cleaning_found.save_cleaning()
            return cleaning_found.json(), 200
        cleaning = CleaningsModel(id, **data)
        cleaning.save_cleaning()
        return cleaning.json(), 201

    def delete(self, id):
        cleaning = CleaningsModel.find_cleaning(id)
        if cleaning:
            try:
                cleaning.delete_cleaning()
            except:
                return {'message': 'An internal error ocurred trying to delete cleaning.'}, 500
            return {'message': 'cleaning deleted.'}
        return {'message': 'cleaning not found.'}, 404
