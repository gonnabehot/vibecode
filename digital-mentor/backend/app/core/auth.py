from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


async def admin_required(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Dummy admin check."""
    token = credentials.credentials
    if token != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
