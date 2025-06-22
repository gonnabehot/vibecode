async def answer_question(query: str) -> dict:
    """Return dummy answer for query."""
    return {"answer": f"Ответ на: {query}", "sources": []}
