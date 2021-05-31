from sqlalchemy.sql.selectable import Join
from database_define import *
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


conn_string = 'sqlite:///partsTrackerAlchemy.db'

engine = create_engine(conn_string)


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

def addTable_Parts(df):
    '''Adds a DataFrame of data into the database'''
    for row in df.iterrows():
        addPart(pn = row['pn'],name = row['name'], qty=row['qty'],commit=False)
    s.commit() 

def shortagelist():
    '''Shows the shortage list for the database'''
    sqlstring = """SELECT pn, (sum(qty)) Total_Required
    FROM PartsList
    GROUP BY pn"""

    sqlstring2 = """SELECT Parts.pn, Parts.qty, totals.Total_Required
    FROM Parts
    INNER JOIN
    (SELECT pn, (sum(qty)) "Total_Required"
    FROM PartsList
    GROUP BY pn) totals
    ON Parts.pn = totals.pn"""

    return pd.read_sql_query(sqlstring2,conn_string)
