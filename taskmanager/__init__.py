import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env # noqa

# Create instance of Flask
app = Flask(__name__)

# Flask application configuration for Secret Key
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# Flask application configuration for DB_URL
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
# Create instance of imported class - Set to instance of Flask app
db = SQLAlchemy(app)

from taskmanager import routes # noqa
