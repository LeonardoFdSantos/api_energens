from sql_alchemy import banco


class InverterModel(banco.Model):
    __tablename__ = 'inverters'

    id = banco.Column(banco.INTEGER, primary_key=True, autoincrement=True)
    customer = banco.Column(banco.String(80))
    numberInverters = banco.Column(banco.INTEGER)
    inverter01 = banco.Column(banco.Float)
    inverter02 = banco.Column(banco.Float)
    inverter03 = banco.Column(banco.Float)
    inverter04 = banco.Column(banco.Float)
    inverter05 = banco.Column(banco.Float)

    def __init__(self, id, customer, numberInverters, inverter01, inverter02, inverter03, inverter04, inverter05):
        self.id = id
        self.customer = customer
        self.numberInverters = numberInverters
        self.inverter01 = inverter01
        self.inverter02 = inverter02
        self.inverter03 = inverter03
        self.inverter04 = inverter04
        self.inverter05 = inverter05

    def json(self):
        return {
            'id': self.id,
            'customer': self.customer,
            'numberInverters': self.numberInverters,
            'inverter01': self.inverter01,
            'inverter02': self.inverter02,
            'inverter03': self.inverter03,
            'inverter04': self.inverter04,
            'inverter05': self.inverter05
        }

    @classmethod
    def find_inverter(cls, id):
        inverter = cls.query.filter_by(id=id).first()
        if inverter:
            return inverter
        return None

    def save_inverter(self):
        banco.session.add(self)
        banco.session.commit()

    def update_inverter(self, customer, numberInverters, inverter01, inverter02, inverter03, inverter04, inverter05):
        self.customer = customer
        self.numberInverters = numberInverters
        self.inverter01 = inverter01
        self.inverter02 = inverter02
        self.inverter03 = inverter03
        self.inverter04 = inverter04
        self.inverter05 = inverter05

    def delete_inverter(self):
        banco.session.delete(self)
        banco.session.commit()
