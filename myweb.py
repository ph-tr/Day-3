from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from program3 import add2, mult2

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/calc/{x}")
async def calculate(request: Request, x: int):
    return templates.TemplateResponse(
        request=request, name="calc.html", context={
            "arg":x, "add2": add2(x), "mult2": mult2(x)
        }
    )