# First Learned how to activate using Powershell after locating script in venv
# .\activate.ps1
# My issue i was not putting the Dot

# Realised i ddn't have a jinja which i had to install learn to install rather

from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware 

from fastapi.templating import Jinja2Templates

app = FastAPI()

# Seting up for jinja2 templates with looks for our templates folder in the dir
templates = Jinja2Templates(directory="templates")

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# recursive guard prohibts me from reading from this line