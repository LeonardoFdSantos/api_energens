from sql_alchemy import banco

class CleaningsModel(banco.Model):
    __tablename__ = 'cleanings'

    id = banco.Column(banco.INTEGER, primary_key=True)
    customer = banco.Column(banco.String(80), primary_key=True)
    date = banco.Column(banco.String(255))
    nextDate = banco.Column(banco.String(255))
    maximumTime = banco.Column(banco.INTEGER)

    def __init__(self, id, customer, date, nextDate, maximumTime):
        self.id = id
        self.customer = customer
        self.date = date
        self.nextDate = nextDate
        self.maximumTime = maximumTime

    def json(self):
        return {
            'id': self.id,
            'customer': self.customer,
            'date': self.date,
            'nextDate': self.nextDate,
            'maximumTime': self.maximumTime,
        }

    @classmethod
    def find_cleaning(cls, id):
        cleaning = cls.query.filter_by(id = id).first()
        if cleaning:
            return cleaning
        return None

    def save_cleaning(self):
        banco.session.add(self)
        banco.session.commit()

    def update_cleaning(self, customer, date, nextDate, maximumTime):
        self.customer = customer
        self.date = date
        self.nextDate = nextDate
        self.maximumTime = maximumTime

    def delete_cleaning(self):
        banco.session.delete(self)
        banco.session.commit()
