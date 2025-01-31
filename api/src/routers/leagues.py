from fastapi import APIRouter
from factories.use_cases import get_upcoming_matches_use_case

leagues_router = APIRouter()

@leagues_router.get("/upcoming-matches")
async def get_upcoming_matches_data():
    try:
        # Call the proper use case to get the data
        matches_data = get_upcoming_matches_use_case()
        return matches_data

    except Exception as e:
        return {"error": str(e)}
