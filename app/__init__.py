from config import Config
from flask import Flask
from flask_migrate import Migrate  # noqa: F401
from flask_sqlalchemy import SQLAlchemy  # noqa: F401

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes  # noqa: F401, E402
