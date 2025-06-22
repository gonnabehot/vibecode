from fastapi import APIRouter
from ..services.qa import answer_question

router = APIRouter(prefix="/ask", tags=["ask"])


@router.post("")
async def ask(payload: dict):
    """Answer user's question."""
    query = payload.get("query", "")
    return await answer_question(query)
