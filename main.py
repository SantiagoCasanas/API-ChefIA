import os

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from typing import Union

from dotenv import load_dotenv

from utils.models import Context, Response
from utils.utils import ask_open_ai
load_dotenv()


app = FastAPI()

origins = os.getenv('origins')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/get-recipe", response_model=Response)
def read_item(context:Context)->Response:
    results = ask_open_ai(context)
    response = Response(message=results)
    return response
