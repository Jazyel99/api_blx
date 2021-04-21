from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token, schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="loginUser")

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
)
data: str = Depends(oauth2_scheme)

def get_current_user(data: str = Depends(oauth2_scheme)):
    return token.verify_token(data, credentials_exception)

async def get_current_active_user(current_user: str = Depends(get_current_user)):
    return current_user.dict()
