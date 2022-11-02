from flask_sqlalchemy import SQLAlchemy
from .controller.rotas import app
from .controller import rotas
from flask_restful import Api

api = Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)