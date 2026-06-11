from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import random
import time
from prometheus_fastapi_instrumentator import Instrumentator
import asyncio

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Hello World"})

@app.get("/heavy")
async def heavy_process():
    random_value = random.randint(1, 5000)
    await asyncio.sleep(random_value / 1000.0)
    
    if random.random() < 0.30:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": "Simulated failure"})

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Success"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

