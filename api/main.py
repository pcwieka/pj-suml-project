from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .schemas import ObesityPredictionRequest, ObesityPredictionResponse
from .model import predict

app = FastAPI()

@app.post("/predict", response_model=ObesityPredictionResponse)
def get_prediction(request: ObesityPredictionRequest):
    prediction = predict(request)
    return JSONResponse(content={"NObeyesdad": prediction})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
