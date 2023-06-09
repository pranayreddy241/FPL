import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from app.schema import IPL as SchemaIPL


from app.schema import IPL


from app.models import IPL as ModelIPL


import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
   return {"message": "IPL world"}


@app.post('/ipl/', response_model=SchemaIPL)
async def ipl(ipl: SchemaIPL):
   db_ipl = ModelIPL(series_id = ipl.series_id,match_id=ipl.match_id,ball_id=ipl.ball_id,inningNumber=ipl.inningNumber,oversActual = ipl.oversActual,overNumber =ipl.overNumber,ballNumber=ipl.ballNumber,totalRuns=ipl.totalRuns,batsman=ipl.batsman,bowler=ipl.bowler,batsmanRuns=ipl.batsmanRuns,isFour=ipl.isFour,isSix=ipl.isSix,isWicket=ipl.isWicket,dismissalType=ipl.dismissalType,byes=ipl.byes,legbyes=ipl.legbyes,wides=ipl.wides,noballs=ipl.noballs,penalties=ipl.penalties,Comment=ipl.Comment)
   db.session.add(db_ipl)
   db.session.commit()
   return db_ipl

@app.get('/ipl/')
async def ipl():
   ipl = db.session.query(ModelIPL).all()
   return ipl


# To run locally
if __name__ == '__main__':
   uvicorn.run(app, host='0.0.0.0', port=8000)