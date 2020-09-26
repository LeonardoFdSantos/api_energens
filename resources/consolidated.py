from flask_restful import Resource, reqparse
from models.consolidated import ConsolidatedModel

class Consolidated(Resource):

    def get(self):
        return {'Consolidated': [consolidated.json() for consolidated in ConsolidatedModel.query.all()]}

class Funded(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('customer', type=str)
    arguments.add_argument('projectNumber', type=int)
    arguments.add_argument('modulesNumber', type=int)
    arguments.add_argument('modulesPower', type=float)
    arguments.add_argument('powerTotal', type=float)
    arguments.add_argument('effectiveness', type=float)
    arguments.add_argument('delivered', type=bool)
    arguments.add_argument('local', type=str)

    def get(self, id):
        consolidated_result = ConsolidatedModel.find_consolidated(id)
        if consolidated_result:
            return consolidated_result.json()
        return {'message': 'Consolidated not found.'}, 404

    def post(self, id):
        if ConsolidatedModel.find_consolidated(id):
            return {"message": "Consolidated id '{}' already exists.".format(id)}, 400
        data = Funded.arguments.parse_args()
        consolidated = ConsolidatedModel(id, **data)
        try:
            consolidated.save_consolidated()
        except:
            return {'message': 'An internal error ocurred trying to save consolidated'}, 500
        return consolidated.json(), 200

    def put(self, id):
        data = Funded.arguments.parse_args()
        consolidated_found = ConsolidatedModel.find_consolidated(id)
        if consolidated_found:
            consolidated_found.update_consolidated(**data)
            consolidated_found.save_consolidated()
            return consolidated_found.json(), 200
        consolidated = ConsolidatedModel(id, **data)
        consolidated.save_consolidated()
        return consolidated.json(), 201

    def delete(self, id):
        consolidated = ConsolidatedModel.find_consolidated(id)
        if consolidated:
            try:
                consolidated.delete_consolidated()
            except:
                return {'message': 'An internal error ocurred trying to delete consolidated.'}, 500
            return {'message': 'Consolidated deleted.'}
        return {'message': 'Consolidated not found.'}, 404
