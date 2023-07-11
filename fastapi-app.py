from fastapi import FastAPI, Request, Body
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

todos = []


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/todos")
async def create_todo(request: Request, toadd: str = Body()):
    print(toadd)
    todos.append(toadd)
    return templates.TemplateResponse(
        "list_items.html", {"request": request, "todos": todos}
    )
