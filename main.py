from typing import Union
from fastapi import FastAPI
from insult import Insult

app = FastAPI()


@app.get("/")
def read_root():
    return {"Danish": "Insulter"}


@app.get("/insult")
def read_item(id: Union[str, None] = None, subject: Union[str, None] = None, unique: bool = False, alliteration: bool = False, log: bool = False):
    insult = Insult(id, subject, unique, alliteration, log)

    insult_response = insult.get_insult()
    error = insult_response[0]
    insult = insult_response[1]
    return {'error': error, 'insult' : insult}
