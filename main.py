from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response
from starlette.responses import JSONResponse

app = FastAPI()

class books:
    author:str
    title:str
    content:str
    creation_datetime:date;

@app.get("/ping")
def getpong ():
    return {f"pong"}

@app.get("/home")
def welcome ():
    with open("welcome.html","r",encoding="utf-8") as file:
        html_content= file.read()
    return Response(content=html_content,status_code=200,media_type="text.html")

@app.get("/{full_path:path}")
def error():
    with open("error.html","r",encoding="utf-8") as file:
        html_content= file.read()
    return Response(content=html_content, status_code=404,media_type="text.html")

@app.post("/posts")
def post_book(books):
    extend(books.author,books.title,books.content,books.creation_datetime)
    if books.author is null:
        return JSONResponse({"The author is missing"},status_code=400)
    elif books.title is null:
        return JSONResponse({f"The title is missing"},status_code=400)
    elif books.content is null:
        return JSONResponse({f"The content is missing"},status_code=400)
    elif books.creation_datetime is null:
        return JSONResponse({f"The creatime is missing"},status_code=400)
    return JSONResponse({f"The book posting is successful"},status_code=200)

@app.get("/posts")
def get_book(books):
    return JSONResponse(
        content={books},
        status_code=200
    )


