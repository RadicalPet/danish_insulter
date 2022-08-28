from typing import Union
from fastapi import FastAPI
from insult import Insult

app = FastAPI()


@app.get("/")
def read_root():
    return {"Danish": "Insulter"}


@app.get("/insult")
def read_item(id: Union[str, None] = None, subject: Union[str, None] = None, unique: bool = False, alliteration: bool = False):
    insult = Insult(id, subject, unique, alliteration)
    return {'insult' : insult.get_insult()}
