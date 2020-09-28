from flask import Flask
from flask_restful import Api
from resources.consolidated import Consolidated, Funded
from resources.inverter import Inverters, Inverter
from resources.customerRegistration import CustomerRegistration, CustomerRegistrations
from resources.accessPassword import AccessPassword, AccessPasswords
from resources.internetPasswords import InternetPassword, InternetPasswords
from resources.cleanings import Cleaning, Cleanings
from resources.localIrradiation import LocalIrradiation, LocationsIrradiation
from resources.predicted import Predicted, Provided

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def createBD():
    banco.create_all()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


api.add_resource(Consolidated, '/consolidated')
api.add_resource(Funded, '/consolidated/<int:id>')
api.add_resource(Inverters, '/inverters')
api.add_resource(Inverter, '/inverters/<int:id>')
api.add_resource(CustomerRegistrations, '/customer')
api.add_resource(CustomerRegistration, '/customer/<int:id>')
api.add_resource(AccessPasswords, '/passwords')
api.add_resource(AccessPassword, '/passwords/<int:id>')
api.add_resource(InternetPasswords, '/internet')
api.add_resource(InternetPassword, '/internet/<int:id>')
api.add_resource(Cleanings, '/cleaning')
api.add_resource(Cleaning, '/cleaning/<int:id>')
api.add_resource(LocationsIrradiation, '/irradiation')
api.add_resource(LocalIrradiation, '/irradiation/<string:city>')
api.add_resource(Predicted, '/predicted')
api.add_resource(Provided, '/predicted/<int:id>')



if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
