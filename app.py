from fastapi import FastAPI
import uvicorn # an asynchronous( concurrent execution where tasks can proceed independently without waiting for other tasks to complete.) server gateway interface
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline


text:str = "what is TextSummarization?"

app = FastAPI()

@app.get("/", tags =["authentication"])
async def index():
    return RedirectResponse(url = "/docs") # when u go for default route it will open "/docs" which will give the fastApI UI

# other two route for train  and predict

@app.get("/train")
async def training():
    try:
        os.system("python main.py") # it run the main.py and run it
        return Response("Training Successful !!")
    
    except Exception as e:
        return Response(f"Error Occured ! {e}")
    

@app.get("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app, host ="0.0.0.0", port =8080)
#  fastapi has default html code 