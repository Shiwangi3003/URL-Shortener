from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
import random
import string

val = ""
val += string.ascii_letters
val += string.digits

app = FastAPI()
store={}


@app.get("/shorturl")
def get_shortened_url(req: str):
    res = ""
    for i in store:
        if store[i]==req:
            return JSONResponse({
                "message" : "Short URL already exists"
            })

    for _ in range(random.randint(3,8)):
        res += random.choice(val)

    store[res] = req
    print(store)
    
    return JSONResponse({
        "message" : "Short URL created",
        "New URL" : res
        })
    

@app.get("/{req}")
def get_full_url(req: str):
    for i in store:
        if i==req:
            return RedirectResponse(store[i])
        
    return JSONResponse({
        "message" : "No such URL found"
    })
