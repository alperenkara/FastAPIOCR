from fastapi import FastAPI,Request
import pathlib
from fastapi import templating 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# D:\GIT\FastAPIOCR\app
BASE_DIR = pathlib.Path(__file__).parent


templates = Jinja2Templates(directory=BASE_DIR/"templates")

# /../app/main.app, app.main.app is a path for the uvicorn
app = FastAPI()

@app.get("/", response_class=HTMLResponse) # HTTP GET
def home_view(request: Request):
    print(request)
    return templates.TemplateResponse("home.html",{"request":request,"secretcode":123})


@app.post("/") # HTTP POST 
def home_detail_view():
    return {"hello":"world"}

