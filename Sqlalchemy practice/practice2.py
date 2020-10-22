from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, ForeignKey

from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class Department(Base):
	__tablename__ = 'department'
	
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	
class Employee(Base):
	__tablename__ = 'employees'
	
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	department_id = Column(Integer, ForeignKey('department.id'))
	
	department = relationship(Department, backref=backref('employee'))
	
	
dep1 = Department(name='IT')
emp1 = Employee(name='Mahalingam', department=dep1)

dep2 = Department(name='Sales')
emp2 = Employee(name='Suresh', department=dep2)
	
engine = create_engine('sqlite:///')
conn = engine.connect()
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()


