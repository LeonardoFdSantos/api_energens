from flask_restful import Resource, reqparse
from models.localIrradiation import LocalIrradiationModel


class LocationsIrradiation(Resource):

    def get(self):
        return {'LocalIrradiation': [localIrradiation.json() for localIrradiation in LocalIrradiationModel.query.all()]}

class LocalIrradiation(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('january', type=float)
    arguments.add_argument('february', type=float)
    arguments.add_argument('march', type=float)
    arguments.add_argument('april', type=float)
    arguments.add_argument('may', type=float)
    arguments.add_argument('june', type=float)
    arguments.add_argument('july', type=float)
    arguments.add_argument('august', type=float)
    arguments.add_argument('september', type=float)
    arguments.add_argument('octuber', type=float)
    arguments.add_argument('november', type=float)
    arguments.add_argument('december', type=float)
    arguments.add_argument('average', type=float)


    def get(self, city):
        localIrradiation = LocalIrradiationModel.find_localIrradiation(city)
        if localIrradiation:
            return localIrradiation.json()
        return {'message': 'Local Irradiation not found.'}, 404

    def post(self, city):
        if LocalIrradiationModel.find_localIrradiation(city):
            return {"message": "Local Irradiation Local id '{}' already exists.".format(city)}, 400
        data = LocalIrradiation.arguments.parse_args()
        localIrradiation = LocalIrradiationModel(city, **data)
        try:
            localIrradiation.save_localIrradiation()
        except:
            return {'message': 'An internal error ocurred trying to save local Irradiation'}, 500
        return localIrradiation.json(), 200

    def put(self, city):
        data = LocalIrradiation.arguments.parse_args()
        localIrradiation_found = LocalIrradiationModel.find_localIrradiation(city)
        if localIrradiation_found:
            localIrradiation_found.update_localIrradiation(**data)
            localIrradiation_found.save_localIrradiation()
            return localIrradiation_found.json(), 200
        localIrradiation = LocalIrradiationModel(city, **data)
        localIrradiation.save_localIrradiation()
        return localIrradiation.json(), 201

    def delete(self, city):
        localIrradiation = LocalIrradiationModel.find_localIrradiation(city)
        if localIrradiation:
            try:
                localIrradiation.delete_localIrradiation()
            except:
                return {'message': 'An internal error ocurred trying to delete Local Irradiation local.'}, 500
            return {'message': 'Local Irradiation local deleted.'}
        return {'message': 'Local Irradiation local not found.'}, 404
