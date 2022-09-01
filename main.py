from typing import Union
from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, tags=["default"])
def read_root(request: Request, insult:bool = False, id:Union[str, None] = None, subject:str = False, unique:bool = False, alliteration:bool = False):
    insult_result=None
    if insult:
        if subject=="me":
            subject=None
        insult = Insult(id=id, subject=subject, unique=unique, alliteration=alliteration)
        try:
            error, id, insult = insult.get_insult()
        except ListExhaustedException as e:
            insult = Insult(id=None, subject=subject, unique=unique, alliteration=alliteration)
            error, id, insult = insult.get_insult()
        insult_result = insult
    return templates.TemplateResponse("insult.html", {"request": request, "id": id, "subject": subject, "unique": unique, "insult_result": insult_result })



@app.get("/nederen", tags=["nederen"])
def read_nederen(
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

@app.get("/historisk/{id}", tags=["historisk"])
def read_item(id):
    print(id)
    insult = Insult(id=id)
    all_insults = insult.get_all_logged_insults()
    return {"insults": all_insults}
