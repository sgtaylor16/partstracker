import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String,DateTime,Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import null

from partsTracker.database_define import *
    
engine = create_engine('sqlite:///partsTrackerAlchemy.db')

from sqlalchemy.orm import sessionmaker

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)