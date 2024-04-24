from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

app = Flask(__name__)
from app import routes


app.secret_key = 'D2T0YkFcSR'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
        db.create_all()