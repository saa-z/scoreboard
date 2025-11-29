from fastapi import FastAPI, Path, Body, Query
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware


class Team(BaseModel):
    name: str
    points: int = Field(0, ge=0)
    sets: int = Field(0, ge=0)


state: list[Team] = [
    Team(name="Home Team"),
    Team(name="Away Team"),
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=list[Team])
async def get_state():
    global state
    return state


@app.put("/scores/{team}", response_model=Team)
async def scores(team: int = Path(..., ge=0, le=1), points: int = Query(None, ge=0), sets: int = Query(None, ge=0)):
    global state
    if points is not None:
        state[team].points = points
    if sets is not None:
        state[team].sets = sets
    return state[team]


@app.put("/names/{team}", response_model=Team)
async def change_name(team: int = Path(..., ge=0, le=1), name: str = Body()):
    global state
    state[team].name = name
    return state[team]


@app.put("/switch", response_model=list[Team])
async def switch():
    global state
    state[1], state[0] = state[0], state[1]
    return state
