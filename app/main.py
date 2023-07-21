from dataclasses import dataclass
from fastapi import FastAPI, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

UPLOAD_DIR = Path() / 'uploads'
templates = Jinja2Templates('templates')

app = FastAPI(debug=True)

@dataclass
class Swimmer:
      name: str
      speed: int

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", 
        context={"request": request, 
                 "name": "testeo",
                 "value": "testeo1234"})

@app.get("/test_htmx", response_class=HTMLResponse)
def test_htmx(request: Request):
    pass

@app.get("/test_jinja2", response_class=HTMLResponse)
def test_jinja2(request: Request):
        return templates.TemplateResponse("projects.html", 
        context={"request": request, 
            "title": "La web del Nano", 
            "projects": ["Project01", "Project02"]})

@app.get("/library", response_class=HTMLResponse)
def library(request: Request):
        return templates.TemplateResponse("library.html", 
        context={"request": request, 
        "textbooks":["Science", "Math", "Algebra", "Music", "Art", "History", "Gym"],
        "magicbooks":["Grim's Traps", "love spells", "Exorcism" ],
        "statement":'<a class="clase1 clase2" href="https://www.imdb.com/name/nm0372117/">Giles</a>',
        "other_title": "<h4>Otro título chico</h4>", 
        "title":"Nano's Server",})

@app.get("/tara", response_class=HTMLResponse)
def tara(request: Request):
        path=request.query_params
        mode=request.query_params._list
        print(mode[0][1])
        print(path)
        return templates.TemplateResponse("tara.html", 
        context={"request": request,  
        "title":"Nano's Server",
        "path": path, 
        "mode": mode[0][1]})

@app.get("/swim", response_class=HTMLResponse)
def swim(request: Request):
    return templates.TemplateResponse("swim.html",
        {"request": request, 
         "swimmers":[
            Swimmer("Cameron", 7),
            Swimmer("Dodd", 6),
            Swimmer("Gage", 8),
            Swimmer("Xander", 5),
        ],
        "title":"Nano's Server"})

@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return "<h1>Home</h1>"

@app.get("/course", response_class=HTMLResponse)
def home(request: Request):
    return "<h1>Home</h1>"


@app.get("/upload_file", response_class=HTMLResponse)
def upload_file(request: Request):
    return templates.TemplateResponse("file_upload.html", {"request": request})


@app.post("/upload_file")
async def create_upload_file(file_uploads: list[UploadFile]):
    for file_upload in file_uploads:
        data = await file_upload.read()
        save_to = UPLOAD_DIR / file_upload.filename
        with open(save_to, 'wb') as f:
            f.write(data)

    return {"filenames": [f.filename for f in file_uploads]}