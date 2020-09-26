from sql_alchemy import banco

class AccessPasswordModel(banco.Model):
    __tablename__ = 'accessPassword'

    id = banco.Column(banco.INTEGER, primary_key=True, autoincrement=True)
    customer = banco.Column(banco.String(80))
    portal = banco.Column(banco.String(255))
    user = banco.Column(banco.String(255))
    password = banco.Column(banco.String(255))


    def __init__(self, id, customer, portal, user, password):
        self.id = id
        self.customer = customer
        self.portal = portal
        self.user = user
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'customer': self.customer,
            'portal': self.portal,
            'user': self.user,
            'password': self.password
        }

    @classmethod
    def find_accessPassword(cls, id):
        accessPassword = cls.query.filter_by(id = id).first()
        if accessPassword:
            return accessPassword
        return None

    def save_accessPassword(self):
        banco.session.add(self)
        banco.session.commit()

    def update_accessPassword(self, customer, portal, user, password):
        self.customer = customer
        self.portal = portal
        self.user = user
        self.password = password

    def delete_accessPassword(self):
        banco.session.delete(self)
        banco.session.commit()
