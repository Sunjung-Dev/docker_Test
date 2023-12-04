from fastapi import FastAPI, Form, Request, Response
from datetime import datetime
import subprocess
import os

app = FastAPI()

@app.get("/")
def main():
    return "Hi"

@app.get("/gru/result")
async def gru_result(text: str):
    path = '/Users/yangayoung/Downloads/gru/main.py'
    subprocess.run(['python3', path, '--input_text', text], text=True)

        
