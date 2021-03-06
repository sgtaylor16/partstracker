
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime,Date, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import null

Base = declarative_base()

class Parts(Base):
    __tablename__ = "Parts"
    pn = Column(String,primary_key=True)
    Name = Column(String,nullable=False)
    Weight = Column(Float,nullable=True)
    qty = Column(Integer,nullable=True)
    M_issue = Column(Boolean,nullable = False)
    F_issue = Column(Boolean,nulable=False)

class Vendors(Base):
    __tablename__ = "Vendors"
    id = Column(Integer,primary_key=True)
    Name = Column(String,nullable=False)

class PartsList(Base):
    __tablename__ = "PartsList"
    fn = Column(Integer,primary_key=True)
    pn = Column(String,ForeignKey("Parts.pn"))
    parts = relationship("Parts",backref= backref("PartsList"))
    qty = Column(Integer,nullable = False)

class Quotes(Base):
    __tablename__ = "Quotes"
    id = Column(Integer,primary_key=True)
    pn = Column(String,ForeignKey("Parts.pn"),nullable=False)
    parts = relationship("Parts",backref=("Quotes"))
    quotedate = Column(Date,nullable=False)
    recurring_cost = Column(Float,nullable=False)
    nre = Column(Float,nullable=False)
    lead_time_wks = Column(Float,nullable = True)
    vendor_id = Column(Integer,ForeignKey("Vendors.id"))
    vendors = relationship("Vendors",backref=backref("Quotes"))

class POs(Base):
    __tablename__ = "POs"
    id = Column(Integer,primary_key="True")
    pn = Column(String,ForeignKey("Parts.pn"))
    parts = relationship("Parts",backref=backref("POs"))
    podate = Column(Date,nullable=False)
    leadtime = Column(Integer,nullable = True)
    recurring_cost = Column(Float,nullable = False)
    nre = Column(Float,nullable=False)
    vendor_id = Column(Integer,ForeignKey("Vendors.id"))
    vendors = relationship("Vendors",backref=backref("POs"))
    sap_po = Column(String,nullable=True)