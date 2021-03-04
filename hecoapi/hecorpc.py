from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
sys.path.append("..")
from hecoscan.models import Session, HecoSwapReward


class Item(BaseModel):
    jsonrpc: str
    method: str
    id: int
    params: list


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/invitation_reward")
async def get_invitation_reward(item: Item):
    if item.method != "hecosearch.invitation.reward" or len(item.params) != 2:
        return []
    session = Session()
    rewards = session.query(HecoSwapReward).filter(
        HecoSwapReward.addr == item.params[0], HecoSwapReward.symbol == item.params[1], HecoSwapReward.subLevel > 0).all()
    return rewards
