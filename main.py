from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def getpong ()
    return ("pong")

@app.get("/home")  
    open("welcome.html","r",encoding="utf-8") as file
        html_content= file.read()
    return Response(content=html_content,status_code=200,media_type="text.html")

@app.get("/{full_path:path}")
    open("welcome.html","r",encoding="utf-8") as file
        html_content= flie.read()
    return Response(content=html_content, status_code=404,media_type="text.html")
        