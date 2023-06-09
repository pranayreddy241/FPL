from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class IPL (Base):
   __tablename__ = 'ipld'
   series_id = Column(Integer)
   match_id = Column(Integer)
   ball_id = Column(Integer, primary_key=True, index=True)
   inningNumber = Column(Integer)
   oversActual = Column(Float)
   overNumber = Column(Integer)
   ballNumber  =Column(Integer)
   totalRuns = Column(Integer)
   batsman = Column(String)
   bowler  = Column(String)
   batsmanRuns =Column(Integer)
   isFour = Column(Boolean)
   isSix  = Column(Boolean)
   isWicket =Column(Boolean)
   dismissalType = Column(Float)
   byes = Column(Integer)
   legbyes =Column(Integer)
   wides =Column(Integer)
   noballs =Column(Integer)
   penalties = Column(Integer)
   Comment = Column(String)
   
