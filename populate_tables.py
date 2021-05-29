from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///partsTrackerAlchemy.db',echo=True)
Base = declarative_base(engine)

class Parts(Base):
    __tablename__ = "Parts"
    __table_args__ = {'autoload':True}

class Vendors(Base):
    __tablename__ = "Vendors"
    __table_args__ = {'autoload':True}

class PartsList(Base):
    __tablename__ = "PartsList"
    __table_args__ = {'autoload':True}

class Quotes(Base):
    __tablename__ = "PartsList"
    __table_args__ = {'autoload':True}

class POs(Base):
    __tablename__ ="PartsList"
    __table_args__ = {'autoload':True}


metadata = Base.metadata
Session = sessionmaker(bind=engine)
s = Session()

##Now add the Data

oneblisk = Parts(pn = '3033072',Name = "4th Stage Blisk")
twoblisk = Parts(pn = '3033067',Name = "1st Stage Blisk")
onevendor = Vendors(Name = 'AdvMfg')
#quote1 = Quotes(pn = '3033072'quotedate = '5/29/21',recurring_cost = 100,nre = 10)

s.add(oneblisk)
s.add(twoblisk)

s.commit()
s.close()

