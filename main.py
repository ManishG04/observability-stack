from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import random
import time


app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Hello World"})

@app.get("/heavy")
def heavy_process():
    random_value = random.randint(1, 5000)
    time.sleep(random_value / 1000.0) 
    
    if random.random() < 0.30:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": "Simulated failure"})

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Success"})

