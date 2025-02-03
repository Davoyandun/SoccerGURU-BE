from fastapi import APIRouter, HTTPException, Depends
from factories.use_cases import get_upcoming_matches_use_case
from core.src.use_cases import GetUpcomingMatches

leagues_router = APIRouter()

@leagues_router.get("/uefa/upcoming-matches")
async def get_upcoming_matches_data(
    use_case: GetUpcomingMatches = Depends(get_upcoming_matches_use_case)
):
    try:
        response_use_case = use_case()

        upcoming_matches = response_use_case.matches

        return (
            [upcoming_match._asdict() for upcoming_match in upcoming_matches]
            if upcoming_matches
            else []
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
