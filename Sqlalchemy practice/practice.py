from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, DateTime, Enum, Numeric

metadata = MetaData()
user_table = Table('user', metadata,
				Column('id', Integer, primary_key=True),
				Column('name', String),
				Column('fullname', String)
			)

fancy_table = Table('fancy', metadata,
				Column('key', String(50), primary_key=True),
				Column('timestamp', DateTime),
				Column('amount', Numeric(10, 2)),
				Column('type', Enum('a', 'b', 'c'))
			)
			
from sqlalchemy import ForeignKey
addresses_table = Table('address', metadata,
					Column('id', Integer, primary_key=True),
					Column('email_address', String(100), nullable=False),
					Column('user_id', Integer, ForeignKey('user.id'))
				)
				
				
network_table = Table('network', metadata,
					Column('network_id', Integer, primary_key=True),
					Column('name', String(100), nullable=False),
					Column('created_at', DateTime, nullable=False),
					Column('owner_id', Integer, ForeignKey('user.id'))
				)
				
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)
metadata.create_all(bind=engine)


metadata2 = MetaData()
user_reflected = Table('user', metadata2, autoload=True, autoload_with=engine)

from sqlalchemy import inspect
inspector = inspect(engine)

network_reflected = Table('network', metadata2, autoload=True, autoload_with=engine)
	
for table in inspector.get_table_names():
	for column in inspector.get_columns(table):
		if column['name'] == 'network_id':
			print(table)

