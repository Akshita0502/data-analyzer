from fastapi import APIRouter
from app.services.aisummary import generate_ai_summary
from app import state

router = APIRouter()

@router.get("/ai-summary")
def aisummary():

    if state.dataset is None:
        return {"error": "no dataset uploaded"}

    df = state.dataset

    summary = generate_ai_summary(df)

    return {"summary": summary}