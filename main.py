from typing import Union

from fastapi import FastAPI

from insulter import Insult

app = FastAPI()


@app.get("/")
def read_root():
    return {"Danish": "Insulter"}


@app.get("/insult")
def read_item(alliteration: Union[str, None] = None):
    
    return
