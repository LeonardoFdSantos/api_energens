from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

banco = SQLAlchemy()
#dialect+driver://username:password@host:port/database
engine = create_engine('mysql://root:1209@localhost:3306/energens-orm')
result = engine.query.all()

for row in result:
    print(row)
