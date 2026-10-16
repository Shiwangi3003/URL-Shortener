from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
import random
import string
import os
from configuration import collection
from database.schema import short_url, response_parser
from fastapi.templating import Jinja2Templates

val = ""
val += string.ascii_letters
val += string.digits

app = FastAPI()
templates = Jinja2Templates(directory="views")
base_url = os.getenv("BASE_URL", "http://localhost:8000").rstrip("/")

@app.get("/")
def home_page(req: Request):
    return templates.TemplateResponse(
        request=req,
        name="index.html",
        context={}
    )


@app.post("/shorturl")
def get_shortened_url(req: str):
    res = ""

    data = collection.find()
    data = response_parser(data) 

    for i in data:
        if i["lurl"] == req:
            return JSONResponse({
                "message" : "Short URL already exists",
                "short_url" : f"{base_url}/{i['surl']}"
            })

    for _ in range(random.randint(3,8)):
        res += random.choice(val)

    collection.insert_one(short_url({
        "surl" : res,
        "lurl" : req
    }))

    return JSONResponse({
        "message" : "Short URL created",
        "short_url" : f"{base_url}/{res}"
    })
    

@app.get("/{req}")
def get_full_url(req: str):

    data = collection.find()
    data = response_parser(data)

    for i in data:
        if i["surl"]==req:
            return RedirectResponse(i["lurl"])
        
    return JSONResponse(status_code=404, content={ "message" : "No such URL found"})
