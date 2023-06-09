# build a schema using pydantic
from pydantic import BaseModel

class IPL(BaseModel):
   series_id:int
   match_id:int
   ball_id:int
   inningNumber : int
   oversActual :float
   overNumber : int
   ballNumber : int
   totalRuns : int
   batsman : str
   bowler  : str
   batsmanRuns : int
   isFour : bool
   isSix : bool
   isWicket : bool
   dismissalType :float
   byes : int
   legbyes : int
   wides : int
   noballs : int
   penalties : int
   Comment : str
   

   class Config:
       orm_mode = True

