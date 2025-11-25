    
class PredictionResponse(BaseModel):
    prediction: int
    probability: List[float]
    depression_risk: str
    feature_feedback: List[Dict[str, Any]]