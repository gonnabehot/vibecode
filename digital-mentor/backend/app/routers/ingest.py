from fastapi import APIRouter, UploadFile, File, Depends
from ..core.auth import admin_required

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.post("", dependencies=[Depends(admin_required)])
async def ingest(file: UploadFile = File(...)):
    """Ingest documents."""
    # Placeholder implementation
    return {"status": "queued", "filename": file.filename}
