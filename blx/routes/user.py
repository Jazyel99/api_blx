from fastapi import APIRouter, Depends, Response, status
from typing import List
from .. import oauth2
from .. import schemas
from .. import database
from .. import models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user


get_db = database.get_db

router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post('/', response_model=schemas.UserView, status_code=status.HTTP_201_CREATED)
def create_new_user(request: schemas.UserBase, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/', status_code=200, response_model=List[schemas.UserView])
def show_all_users(db: Session = Depends(get_db), current_user: schemas.UserView = Depends(oauth2.get_current_user)):
    return user.show(db)

@router.get('/{id}', status_code=200, response_model= schemas.UserView)
def show_user(id: str,db: Session = Depends(get_db)):
    return user.show_id(id, db)