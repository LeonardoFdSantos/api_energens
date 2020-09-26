from flask_restful import Resource, reqparse
from models.predicted import ProvidedModel


class Predicted(Resource):

    def get(self):
        return {'Predicted': [predicted.json() for predicted in ProvidedModel.query.all()]}

class Provided(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('customer', type=str)
    arguments.add_argument('effectiveness', type=float)
    arguments.add_argument('powerTotal', type=float)
    arguments.add_argument('local', type=str)
    arguments.add_argument('january', type=int)
    arguments.add_argument('february', type=int)
    arguments.add_argument('march', type=int)
    arguments.add_argument('april', type=int)
    arguments.add_argument('may', type=int)
    arguments.add_argument('june', type=int)
    arguments.add_argument('july', type=int)
    arguments.add_argument('august', type=int)
    arguments.add_argument('september', type=int)
    arguments.add_argument('october', type=int)
    arguments.add_argument('november', type=int)
    arguments.add_argument('december', type=int)
    arguments.add_argument('average', type=float)


    def get(self, id):
        provided = ProvidedModel.find_provided(id)
        if provided:
            return provided.json()
        return {'message': 'Predicted not found.'}, 404

    def post(self, id):
        if ProvidedModel.find_provided(id):
            return {"message": "Predicted id '{}' already exists.".format(id)}, 400
        data = Provided.arguments.parse_args()
        provided = ProvidedModel(id, **data)
        try:
            provided.save_provided()
        except:
            return {'message': 'An internal error ocurred trying to save Predicted'}, 500
        return provided.json(), 200

    def put(self, id):
        data = Provided.arguments.parse_args()
        provided_found = ProvidedModel.find_provided(id)
        if provided_found:
            provided_found.update_provided(**data)
            provided_found.save_provided()
            return provided_found.json(), 200
        provided = ProvidedModel(id, **data)
        provided.save_provided()
        return provided.json(), 201

    def delete(self, id):
        provided = ProvidedModel.find_provided(id)
        if provided:
            try:
                provided.delete_provided()
            except:
                return {'message': 'An internal error ocurred trying to delete Predicted.'}, 500
            return {'message': 'Predicted deleted.'}
        return {'message': 'Predicted not found.'}, 404
