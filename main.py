from fastapi import FastAPI
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Synthesia import Synthesia
from fastapi import Request
import requests
from models import Solardata
templates_engine = Jinja2Templates(directory="templates")

app = FastAPI()
synth = Synthesia()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/templates_html", response_class=HTMLResponse)
async def get_templates_html(request: Request):
    template_data = synth.ListTemplates()
    return templates_engine.TemplateResponse(
        "templates_list.html",  # Name of your HTML template file
        {
            "request": request,
            "templates": template_data
        }
    )
@app.get("/templates")
async def get_templates():
    templates = synth.ListTemplates()
    # Just return them directly as JSON
    return {"templates": templates}
@app.get("/template/{template_id}")
async def get_template(template_id: str):
    template = synth.retrieveTemplate(template_id)
    return template
@app.post("/create_video")
async def create_video(data: Solardata):
    data = synth.Create_video_template(data)
    return data
@app.get("/get_video/{video_id}")
async def get_video(video_id: str):
    data = synth.Get_video(video_id)
    return data
