from flask import Flask, request, jsonify
from flask_restful import Resource
from ..model import Tables as md

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

class Employees(Resource):
    def get(delf):
        employees = md.db_session.query(md.Employee).all()
        response = [{'id': i.id, 'name': i.name, 'email': i.email,
                'phone': i.phone, 'document': i.document} for i in employees]
        if response == []: return "Nada econtrado."
        return jsonify(response)
    
    def post(delf):
        data = request.json
        employee = md.Employee(
            name=data['name'], email=data['email'], phone=data['phone'], document=data['document'])
        employee.save()
        response = {
                'id': employee.id,
                'name': employee.name,
                'email': employee.email,
                'phone': employee.phone,
                'document': employee.document,
        }
        return response

class Employee(Resource):
    def get(delf, employee_id):
        employee = md.db_session.query(md.Employee).filter_by(id=employee_id).first()
        deps = md.db_session.query(md.Dependent).filter_by(id_employee=employee_id).all()
        try:
            response = {'id': employee.id, 'name': employee.name, 'email': employee.email,
                    'phone': employee.phone, 'document': employee.document, 
                    'dependents': [{'id': i.id, 'name': i.name}for i in deps]}
        except AttributeError:
            response = {
                'status': 'error',
                'msg': 'Func não encontrado'
            }
        return response



class Dependents(Resource):
    def get(delf):
        dependents = md.db_session.query(md.Dependent).all()
        response = [{'id': i.id, 'name': i.name, 'id_employee': i.id_employee,
                } for i in dependents]
        if response == []: return "Nada econtrado."
        return jsonify(response)
    
    def post(delf):
        data = request.json
        dependent = md.Dependent(
            name=data['name'], id_employee=data['id_employee'])
        dependent.save()
        response = {
                'id': dependent.id,
                'name': dependent.name,
                'id_employee': dependent.id_employee,
        }
        return response