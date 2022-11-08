from flask_sqlalchemy import SQLAlchemy
from .controller.rotas import app
from .controller import rotas as rotas
from flask_restful import Api

api = Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)

api.add_resource(rotas.Employees, '/employees')
api.add_resource(rotas.Employee, '/employees/<int:employee_id>')

api.add_resource(rotas.Dependents, '/dependents')