from sql_alchemy import banco


class CustomerRegistrationModel(banco.Model):
    __tablename__ = 'customerregistration'

    id = banco.Column(banco.INTEGER, primary_key=True)
    customer = banco.Column(banco.String(80), primary_key=True)
    typeCustomer = banco.Column(banco.String(255))
    CPF_CNPJ = banco.Column(banco.String(45))
    code = banco.Column(banco.String(45))

    def __init__(self, id, customer, typeCustomer, CPF_CNPJ, code):
        self.id = id
        self.customer = customer
        self.typeCustomer = typeCustomer
        self.CPF_CNPJ = CPF_CNPJ
        self.code = code

    def json(self):
        return {
            'id': self.id,
            'customer': self.customer,
            'typeCustomer': self.typeCustomer,
            'CPF_CNPJ': self.CPF_CNPJ,
            'code': self.code
        }

    @classmethod
    def find_customerRegistration(cls, id):
        registro_customer = cls.query.filter_by(id=id).first()
        if registro_customer:
            return registro_customer
        return None

    def save_customerRegistration(self):
        banco.session.add(self)
        banco.session.commit()

    def update_customerRegistration(self, customer, typeCustomer, CPF_CNPJ, code):
        self.customer = customer
        self.typeCustomer = typeCustomer
        self.CPF_CNPJ = CPF_CNPJ
        self.code = code

    def delete_customerRegistration(self):
        banco.session.delete(self)
        banco.session.commit()
