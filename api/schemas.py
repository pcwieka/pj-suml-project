from pydantic import BaseModel

class ObesityPredictionRequest(BaseModel):
    Gender: str
    Age: int
    Height: float
    Weight: float
    family_history_with_overweight: str
    FAVC: str
    FCVC: int
    NCP: int
    CAEC: str
    SMOKE: str
    CH2O: int
    SCC: str
    FAF: int
    TUE: int
    CALC: str
    MTRANS: str

class ObesityPredictionResponse(BaseModel):
    NObeyesdad: str
