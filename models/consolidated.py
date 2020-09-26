from sql_alchemy import banco


class ConsolidatedModel(banco.Model):
    __tablename__ = 'consolidados'

    id = banco.Column(banco.INTEGER, primary_key=True, autoincrement=True)
    customer = banco.Column(banco.String(80))
    projectNumber = banco.Column(banco.INTEGER)
    modulesNumber = banco.Column(banco.INTEGER)
    modulesPower = banco.Column(banco.Float)
    powerTotal = banco.Column(banco.Float)
    effectiveness = banco.Column(banco.Float(precision=2))
    delivered = banco.Column(banco.Boolean, default=False)
    local = banco.Column(banco.String(80))

    def __init__(self, id, customer, projectNumber, modulesNumber, modulesPower, powerTotal, effectiveness, delivered,
                 local):
        self.id = id
        self.customer = customer
        self.projectNumber = projectNumber
        self.modulesNumber = modulesNumber
        self.modulesPower = modulesPower
        self.powerTotal = powerTotal
        self.effectiveness = effectiveness
        self.delivered = delivered
        self.local = local

    def json(self):
        return {
            'id': self.id,
            'customer': self.customer,
            'projectNumber': self.projectNumber,
            'modulesNumber': self.modulesNumber,
            'modulesPower': self.modulesPower,
            'powerTotal': self.powerTotal,
            'effectiveness': self.effectiveness,
            'delivered': self.delivered,
            'local': self.local
        }

    @classmethod
    def find_consolidated(cls, id):
        consolidated = cls.query.filter_by(id=id).first()
        if consolidated:
            return consolidated
        return None

    def save_consolidated(self):
        banco.session.add(self)
        banco.session.commit()

    def update_consolidated(self, customer, projectNumber, modulesNumber, modulesPower, powerTotal, effectiveness,
                            delivered, local):
        self.customer = customer
        self.projectNumber = projectNumber
        self.modulesNumber = modulesNumber
        self.modulesPower = modulesPower
        self.powerTotal = powerTotal
        self.effectiveness = effectiveness
        self.delivered = delivered
        self.local = local

    def delete_consolidated(self):
        banco.session.delete(self)
        banco.session.commit()
