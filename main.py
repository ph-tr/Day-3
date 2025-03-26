from typing import Union

from fastapi import FastAPI

from program3 import add2, mult2

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/add2/{arg}")
def add2_handler(arg:int):
    return {"arg": arg, "add2": add2(arg)}

@app.get("/mult2/{arg}")
def mult2_handler(arg:int):
    return {"arg": arg, "mult2": mult2(arg)}