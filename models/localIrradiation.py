from sql_alchemy import banco

class LocalIrradiationModel(banco.Model):
    __tablename__ = 'localirradiation'

    city = banco.Column(banco.String(80), primary_key=True)
    january = banco.Column(banco.Float)
    february = banco.Column(banco.Float)
    march = banco.Column(banco.Float)
    april = banco.Column(banco.Float)
    may = banco.Column(banco.Float)
    june = banco.Column(banco.Float)
    july = banco.Column(banco.Float)
    august = banco.Column(banco.Float)
    september = banco.Column(banco.Float)
    october = banco.Column(banco.Float)
    november = banco.Column(banco.Float)
    december = banco.Column(banco.Float)
    average = banco.Column(banco.Float)

    def __init__(self, city, january, february, march, april, may, june, july, august, september, october, november, december, average):
        self.city = city
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
            'city': self.city,
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
    def find_localIrradiation(cls, city):
        localIrradiation = cls.query.filter_by(city = city).first()
        if localIrradiation:
            return localIrradiation
        return None

    def save_localIrradiation(self):
        banco.session.add(self)
        banco.session.commit()

    def update_localIrradiation(self, january, february, march, april, may, june, july, august, september, october, november, december, average):
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

    def delete_localIrradiation(self):
        banco.session.delete(self)
        banco.session.commit()
