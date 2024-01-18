from config import Config
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate  # noqa: F401
from flask_sqlalchemy import SQLAlchemy  # noqa: F401

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"
from app import models, routes  # noqa: F401, E402
