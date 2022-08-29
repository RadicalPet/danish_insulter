from typing import Union

from fastapi import FastAPI

from insult import Insult

app = FastAPI()


@app.get("/")
def read_root():
    return {"Danish": "Insulter"}


@app.get("/besudlet")
def read_item(
    id: Union[str, None] = None,
    subject: Union[str, None] = None,
    unique: bool = False,
    alliteration: bool = False,
    nolog: bool = False,
):
    insult = Insult(id, subject, unique, alliteration, nolog)

    error, id, insult = insult.get_insult()
    return {"error": error, "id": id, "insult": insult}
