from flask_restful import Resource, reqparse
from models.inverter import InverterModel


class Inverters(Resource):

    def get(self):
        return {'Inverters': [inverter.json() for inverter in InverterModel.query.all()]}

class Inverter(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('cliente', type=str)
    arguments.add_argument('num_inverter', type=int)
    arguments.add_argument('inverter01', type=float)
    arguments.add_argument('inverter02', type=float)
    arguments.add_argument('inverter03', type=float)
    arguments.add_argument('inverter04', type=float)
    arguments.add_argument('inverter05', type=bool)


    def get(self, id):
        inverter = InverterModel.find_inverter(id)
        if inverter:
            return inverter.json()
        return {'message': 'Inverter not found.'}, 404

    def post(self, id):
        if InverterModel.find_inverter(id):
            return {"message": "Inverter id '{}' already exists.".format(id)}, 400
        data = Inverter.arguments.parse_args()
        inverter = InverterModel(id, **data)
        try:
            inverter.save_inverter()
        except:
            return {'message': 'An internal error ocurred trying to save inverter'}, 500
        return inverter.json(), 200

    def put(self, id):
        data = Inverter.arguments.parse_args()
        inverter_found = InverterModel.find_inverter(id)
        if inverter_found:
            inverter_found.update_inverter(**data)
            inverter_found.save_inverter()
            return inverter_found.json(), 200
        inverteres = InverterModel(id, **data)
        inverteres.save_inverter()
        return inverteres.json(), 201

    def delete(self, id):
        inverter = InverterModel.find_inverter(id)
        if inverter:
            try:
                inverter.delete_inverter()
            except:
                return {'message': 'An internal error ocurred trying to delete inverter.'}, 500
            return {'message': 'Inverter deleted.'}
        return {'message': 'Inverter not found.'}, 404
