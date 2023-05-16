from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = '19b253df6e070936e5e83ba04d6e04c7'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://comunidadeimpressionadora:OqCwB30dzmso5l2hIyfasuuTDuOnReAQ@dpg-chhah9u4dad31tjuoncg-a/comunidadeimpressionadora'    

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça o login para ter acesso'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import models
engine = sqlalchemy.create_engine('sqlite:///comunidade.db')
inspect = sqlalchemy.inspect(engine)
if not inspect.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de dados criada")
        print("Deu ruim no BD")
else:
    print("Base de dados já existente")
print(app.config['SQLALCHEMY_DATABASE_URI'])
print(os.getenv("DATABASE_URL"))

from comunidadeimpressionadora import routes
