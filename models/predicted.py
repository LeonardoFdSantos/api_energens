from sql_alchemy import banco

class ProvidedModel(banco.Model):
    __tablename__ = 'provided'

    id = banco.Column(banco.INTEGER, primary_key=True, autoincrement=True)
    customer = banco.Column(banco.String(80))
    effectiveness = banco.Column(banco.Float(precision=2))
    powerTotal = banco.Column(banco.Float)
    local = banco.Column(banco.String(80))
    january = banco.Column(banco.INTEGER)
    february = banco.Column(banco.INTEGER)
    march = banco.Column(banco.INTEGER)
    april = banco.Column(banco.INTEGER)
    may = banco.Column(banco.INTEGER)
    june = banco.Column(banco.INTEGER)
    july = banco.Column(banco.INTEGER)
    august = banco.Column(banco.INTEGER)
    september = banco.Column(banco.INTEGER)
    october = banco.Column(banco.INTEGER)
    november = banco.Column(banco.INTEGER)
    december = banco.Column(banco.INTEGER)
    average = banco.Column(banco.Float)

    def __init__(self,id, customer, effectiveness, powerTotal, local, january, february, march, april, may, june, july, august, september, october, november, december, average):
        self.id = id
        self.customer = customer
        self.effectiveness = effectiveness
        self.powerTotal = powerTotal
        self.local = local
        self.january = january
        self.february = february
        self.march = march
        self.april = april
        self.may = may
        self.june = june
        self.july = july
        self.august = august
        self.september = september
        self.october = october
        self.november = november
        self.december = december
        self.average = average

    def json(self):
        return {
            'id': self.id,
            'customer': self.customer,
            'effectiveness': self.effectiveness,
            'powerTotal': self.powerTotal,
            'local': self.local,
            'january': self.january,
            'february': self.february,
            'march': self.march,
            'april': self.april,
            'may': self.may,
            'june': self.june,
            'july': self.july,
            'august': self.august,
            'september': self.september,
            'october': self.october,
            'november': self.november,
            'december': self.december,
            'average': self.average
        }

    @classmethod
    def find_provided(cls, id):
        previsto = cls.query.filter_by(id = id).first()
        if previsto:
            return previsto
        return None

    def save_provided(self):
        banco.session.add(self)
        banco.session.commit()

    def update_provided(self, customer, effectiveness, powerTotal, local, january, february, march, april, may, june, july, august, september, october, november, december, average):
        self.customer = customer
        self.effectiveness = effectiveness
        self.powerTotal = powerTotal
        self.local = local
        self.january = january
        self.february = february
        self.march = march
        self.april = april
        self.may = may
        self.june = june
        self.july = july
        self.august = august
        self.september = september
        self.october = october
        self.november = november
        self.december = december
        self.average = average

    def delete_provided(self):
        banco.session.delete(self)
        banco.session.commit()
