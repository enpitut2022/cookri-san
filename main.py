from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Union
import json

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("main.html", {"request":request})

@app.get("/result/", response_class=HTMLResponse)
async def result(request:Request, ing:Union[List[str], None] = Query(default=None)):
    json_open = open('fixture/recipe.json', mode = 'r', encoding = 'UTF-8')
    json_load = json.load(json_open)
    recipe = []
    for i in json_load:
        for item in ing:
            if item in i["tags"]:
                recipe.append(i)
    #recipe = dict(set(recipe))
    return templates.TemplateResponse("result.html", {"request":request, "ing":ing, "recipe":recipe})