from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db00.sqlite', connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base()