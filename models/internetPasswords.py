from sql_alchemy import banco

class InternetPasswordsModel(banco.Model):
    __tablename__ = 'internetPasswords'

    id = banco.Column(banco.INTEGER, primary_key=True)
    customer = banco.Column(banco.String(80), primary_key=True)
    ssid = banco.Column(banco.String(255))
    password = banco.Column(banco.String(255))


    def __init__(self, id, customer, ssid, password):
        self.id = id
        self.customer = customer
        self.ssid = ssid
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'customer': self.customer,
            'ssid': self.ssid,
            'password': self.password
        }

    @classmethod
    def find_internetPassword(cls, id):
        internetPassword = cls.query.filter_by(id = id).first()
        if internetPassword:
            return internetPassword
        return None

    def save_internetPassword(self):
        banco.session.add(self)
        banco.session.commit()

    def update_internetPassword(self, customer, ssid, password):
        self.customer = customer
        self.ssid = ssid
        self.password = password

    def delete_internetPassword(self):
        banco.session.delete(self)
        banco.session.commit()
