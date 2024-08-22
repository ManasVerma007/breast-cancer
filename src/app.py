from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from  models.prediction_model import Prediction_Model


templates =  Jinja2Templates(directory="src/templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@ app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(name= "index.html", request=request)


@ app.post("/predict")
async def predict(request: Request):
    form = dict(await request.form())   
    model = Prediction_Model(form)
    result = "Malignant" if  model.predict() == 1 else "Benign"
    return templates.TemplateResponse("result.html", {"request": request, "result": result})



if __name__ == "__main__":
    uvicorn.run(app=app, port=8000)