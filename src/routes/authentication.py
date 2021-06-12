from fastapi import APIRouter, Depends, HTTPException, status
from ..auth.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from ..infra.sqlalchemy.config import database
from ..infra.sqlalchemy.models import models
from ..auth import token

from sqlalchemy.orm import Session
import json

router = APIRouter(
    tags=['Authentication']
)

@router.post('/loginUser')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.user_name == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Credentials')
    if not Hash.verify(user.user_password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Incorrect password')
    
    #generate a jwt token and return
    access_token = token.create_access_token(data={"sub": user.user_name, "user_id": user.user_id})

    return {"access_token": access_token, "token_type": "bearer"}