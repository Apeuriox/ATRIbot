from fastapi import FastAPI

from pydantic import BaseModel
from typing import Optional

import ATRIhandle

import uvicorn


app = FastAPI()

atri=ATRIhandle.ATRI()

class Item(BaseModel):
    osuname: str

@app.api_route("/info", methods=["GET", "POST"])
async def get_user_info(item: Item):
    result=atri.get_user(item.osuname)
    print(result)
    return result

@app.api_route("/choke", methods=["GET", "POST"])
async def get_choke_info(item: Item):
    result=await atri.get_choke(item.osuname)
    print(result)
    return result

@app.api_route("/test", methods=["GET", "POST"])
async def test():
    result=await atri.test()

if __name__=='__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)