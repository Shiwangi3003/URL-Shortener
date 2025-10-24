from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
import random
import string
from configuration import collection
from database.schema import short_url, response_parser

val = ""
val += string.ascii_letters
val += string.digits

app = FastAPI()


@app.get("/shorturl")
def get_shortened_url(req: str):
    res = ""

    data = collection.find()
    data = response_parser(data)

    for i in data:
        if i["lurl"] == req:
            return JSONResponse({
                "message" : "Short URL already exists"
            })

    for _ in range(random.randint(3,8)):
        res += random.choice(val)

    collection.insert_one(short_url({
        "surl" : res,
        "lurl" : req
    }))

    return JSONResponse({
        "message" : "Short URL created",
        "New URL" : "https://url-shortener-2q3m.onrender.com/"+res
    })
    

@app.get("/{req}")
def get_full_url(req: str):

    data = collection.find()
    data = response_parser(data)

    for i in data:
        if i["surl"]==req:
            return RedirectResponse(i["lurl"])
        
    return JSONResponse({
        "message" : "No such URL found"
    })
