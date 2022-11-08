from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.db import *

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    document = Column(Integer, nullable=False)
    dependents = relationship('Dependent', backref='employees', lazy='dynamic')
    
    def __init__(self, name, email, phone, document):
        self.name= name
        self.email= email
        self.phone= phone
        self.document = document

    def __repr__(self):
        return "<Employee: {}>".format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Dependent(Base):
    __tablename__ = 'dependents'
    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    id_employee=Column(Integer, ForeignKey('employees.id'))

    def __init__(self, name, id_employee):
        self.name= name
        self.id_employee= id_employee

    def __repr__(self):
        return "<Dependent: {}>".format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
