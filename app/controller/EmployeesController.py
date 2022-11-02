from flask import Flask, request, jsonify
from flask_restful import Resource
from ..model import Employess as md

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

class Employee(Resource):
    def get(delf):
        employees = md.db_session.query(md.Employees).all()
        response = [{'id': i.id, 'name': i.name, 'email': i.email,
                'cel': i.cel} for i in employees]
        if response == []: return "Nada econtrado."
        return jsonify(response)
    
    def post(delf):
        data = request.json
        employee = md.Employees(
            name=data['name'], email=data['email'], cel=data['cel'])
        employee.save()
        response = {
                'id': employee.id,
                'name': employee.name,
                'email': employee.email,
                'cel': employee.cel,
        }
        return response