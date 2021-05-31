from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from partsTracker.database_define import *

engine = create_engine('sqlite:///partsTrackerAlchemy.db')

#metadata = Base.metadata
Session = sessionmaker(bind=engine)
s = Session()

##Now add the Data

## Add the Parts
s.add_all([
    Parts(pn= '3033072', Name='4th Stage Blisk',qty =0),
    Parts(pn= '3033067', Name = '1st Stage Blisk',qty=0),
    Parts(pn='AS478-10', Name = 'Bolt',qty = 5),
    Parts(pn='AN10',Name = 'Nut',qty =1)
])

## Add the Parts List

s.add_all([
    PartsList(fn=1,pn='3033072',qty = 1),
    PartsList(fn=2,pn='3033067',qty =1),
    PartsList(fn=3,pn='AS478-10',qty=10),
    PartsList(fn=4,pn='AN10',qty=10),
    PartsList(fn=5,pn='AS478-10',qty=4)
])

# Add the Vendors

s.add(Vendors(Name = 'AdvMfg'))

# Add the POs

 
s.commit()
s.close()

