from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import date

class InsightResponse(BaseModel):
    top_stress_features: List[str]
    correlations: Dict[str, float]

class DailyInsightOut(BaseModel):
    date: date
    avg_stress: float
    notes: Optional[str] = None
