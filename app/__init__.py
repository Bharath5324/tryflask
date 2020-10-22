from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import flask_monitoringdashboard as dashboard
# from flask_restful import Api

app = Flask(__name__)
login = LoginManager(app)
dashboard.config.init_from(file='../config.cfg')
dashboard.bind(app)
# api = Api(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models