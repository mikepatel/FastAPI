"""
Michael Patel
July 2022

Project description:

File description:

"""
################################################################################
# Imports
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


################################################################################
class Player(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    team: Optional[str]


################################################################################
app = FastAPI()


@app.get("/")
async def index():
    return str(datetime.now())


@app.get("/player")
async def get_player():
    player = Player(
        first_name="Joel",
        last_name="Embiid",
        team="76ers"
    )
    output = f'Getting player --> {player.first_name} {player.last_name} of the {player.team}'
    return output


@app.post("/player")
async def create_player(player: Player):
    output = f'Creating a new player called {player.first_name} {player.last_name} who plays for the {player.team}'
    return output


################################################################################
# Main
