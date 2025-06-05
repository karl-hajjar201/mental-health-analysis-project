from fastapi import APIRouter
from models import InsightResponse
from fastapi import APIRouter, HTTPException, Query
from datetime import date
from db import SessionLocal, DailyInsight
from models import DailyInsightOut
router = APIRouter()

INSIGHTS = {
    "top_stress_features": [
        "mental_health_status",
        "air_quality_index",
        "sleep_hours"
    ],
    "correlations": {
        "mental_health_status": 0.83,
        "air_quality_index": 0.56,
        "sleep_hours": -0.44
    }
}

@router.get("/mental-insights", response_model=InsightResponse)
def get_mental_insights():
    return INSIGHTS


@router.get("/daily-insight", response_model=DailyInsightOut)
def get_daily_insight(date: date = Query(..., description="Date in YYYY-MM-DD format")):
    db = SessionLocal()
    result = db.query(DailyInsight).filter(DailyInsight.date == date).first()
    db.close()
    if not result:
        raise HTTPException(status_code=404, detail=f"No insights found for {date}")
    return DailyInsightOut(
        date=result.date,
        avg_stress=result.avg_stress,
        notes=result.notes
    )
