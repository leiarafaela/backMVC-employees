from flask_sqlalchemy import SQLAlchemy
from .controller.EmployeesController import app
from .controller import EmployeesController as rotas
from flask_restful import Api

api = Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)

api.add_resource(rotas.Employee, '/employees')