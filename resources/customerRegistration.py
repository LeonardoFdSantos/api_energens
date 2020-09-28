from flask_restful import Resource, reqparse
from models.customerRegistration import CustomerRegistrationModel


class CustomerRegistrations(Resource):

    def get(self):
        return {'CustomerRegistration': [customerRegistration.json() for customerRegistration in
                                          CustomerRegistrationModel.query.all()]}


class CustomerRegistration(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('customer', type=str)
    arguments.add_argument('typeCustomer', type=str)
    arguments.add_argument('CPF_CNPJ', type=str)
    arguments.add_argument('code', type=str)

    def get(self, id):
        customerRegistration = CustomerRegistrationModel.find_customerRegistration(id)
        if customerRegistration:
            return customerRegistration.json()
        return {'message': 'Customer Registration not found.'}, 404

    def post(self, id):
        if CustomerRegistrationModel.find_customerRegistration(id):
            return {"message": "Customer Registration id '{}' already exists.".format(id)}, 400
        data = CustomerRegistration.arguments.parse_args()
        customerRegistration = CustomerRegistrationModel(id, **data)
        try:
            customerRegistration.save_customerRegistration()
        except:
            return {'message': 'An internal error ocurred trying to save Customer Registration'}, 500
        return customerRegistration.json(), 200

    def put(self, id):
        data = CustomerRegistration.arguments.parse_args()
        customerRegistration_found = CustomerRegistrationModel.find_customerRegistration(id)
        if customerRegistration_found:
            customerRegistration_found.update_customerRegistration(**data)
            customerRegistration_found.save_customerRegistration()
            return customerRegistration_found.json(), 200
        customerRegistration = CustomerRegistrationModel(id, **data)
        customerRegistration.save_customerRegistration()
        return customerRegistration.json(), 201

    def delete(self, id):
        customerRegistration = CustomerRegistrationModel.find_customerRegistration(id)
        if customerRegistration:
            try:
                customerRegistration.delete_customerRegistration()
            except:
                return {'message': 'An internal error ocurred trying to delete Customer Registration.'}, 500
            return {'message': 'Customer Registration deleted.'}
        return {'message': 'Customer Registration not found.'}, 404
