from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

manager = flask.ext.restless.APIManager(app,  flask_sqlalchemy_db=db)

from really.views import aview
from really.models import Project, Issue

manager.create_api(Project, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Issue, methods=['GET', 'POST', 'DELETE'])