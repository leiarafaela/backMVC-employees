from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.db import *

Base = declarative_base()

class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(30), nullable=False)
    cel = Column(String(20), nullable=False)
    

    def __init__(self, name, email, cel):
        self.name= name
        self.email= email
        self.cel= cel

    def __repr__(self):
        return "<Employee: {}>".format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()