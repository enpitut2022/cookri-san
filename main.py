from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Union, Set
import json

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("main.html", {"request":request})

@app.get("/result/", response_class=HTMLResponse)
async def result(request:Request, ing:Set[str] = Query(default=set()), search_not:Set[str] = Query(default=set())):
    json_open = open('fixture/recipe2.json', mode = 'r', encoding = 'UTF-8')
    json_load = json.load(json_open)
    recipe = []
    recipe_or = []

    #urls = []
    # ing = ["鶏もも肉", "ピーマン"]　⇚　main.htmlで2つ以上入力したとき
    # ing = ["鶏もも肉 ピーマン"]　⇚ result.htmlで2つ入力したとき
    if len(ing) == 1:
        ing = set(list(ing)[0].split())
    for i in json_load:
        if len(search_not) != 0:
            query_not = list(search_not)[0].split()
            query_not = set(query_not)
            if set(i["tags"]) & ing == ing and set(i["tags"]) & query_not == set():
                recipe.append(i)
            if ing-set(i["tags"]) != ing and set(i["tags"]) & query_not == set():
                recipe_or.append(i)
        else:
            search_not = set()
            if set(i["tags"]) & ing == ing:
                recipe.append(i)
            if ing-set(i["tags"]) != ing and set(i["tags"]):
                recipe_or.append(i)

    #recipe.extend(recipe_or)
    ing_s = " ".join(list(ing))
    not_s = " ".join(list(search_not))
    return templates.TemplateResponse("result.html", {"request":request, "ing":list(ing), "recipe":recipe, "recipe_or":recipe_or, "ing_s":ing_s, "not_s": not_s, "search_not": list(search_not)})