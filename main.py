from typing import Union

from fastapi import FastAPI, Query

from insult import *

tags_metadata = [
    {
        "name": "nederen",
        "description": "request a Danish insult",
    },
    {
        "name": "historisk",
        "description": "get insult history for an id"
    }
]

app = FastAPI(openapi_tags=tags_metadata)


@app.get("/")
def read_root():
    return {"Danish": "Insulter"}


@app.get("/nederen")
def read_item(
    id: Union[str, None] =  Query(None, description="uuid to log the insult to - a uuid gets generated with every request without this parameter", ),
    subject: Union[str, None] =  Query(None, description='add subject for the insult (han/hen/hun/min chef etc.) - default is "du"', ),
    unique: bool = Query(False, description='keep insult values unique to uuid until shortest list exhausted', ),

    alliteration: bool = Query(False, description='will us alliterations where possible', ),
    nolog: bool = Query(False, description='do not log insult - nolog false required by unique', ),

):
    insult = Insult(id, subject, unique, alliteration, nolog)
    try:
        error, id, insult = insult.get_insult()
    except ListExhaustedException as e:
        return {"error": e, "id": id, "insult": None}
    return {"error": error, "id": id, "insult": insult}
