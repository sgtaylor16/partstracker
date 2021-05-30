from database_define import *

addParts(qty)

engine = create_engine('sqlite:///partsTrackerAlchemy.db')


Session = sessionmaker(bind=engine)
s = Session()

def addPart(pn,name,qty,weight=None,checkdb = True,commit=True):
    '''
    Function to add a part to the database. Wrapper around SqlAlchemy
    Keyword Arguments:
    pn (string):  string pn in the parts table
    name (string): name of part
    qty (int): number of parts on hand.
    weight(float): - weight of part
    '''
    #Check to make sure pn is unique
    if checkdb is True:
        results = s.query(Parts).filter(pn=pn).all()
        pns = [x.pn for x in results]
        if pn in pns:
            return '{0} Already in Database'
    s.add(Parts(pn=pn,Name=name,qty=qty))
    if commit is True:
        s.commit()
    return None



