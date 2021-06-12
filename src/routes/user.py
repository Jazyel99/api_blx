from fastapi import APIRouter, Depends, Response, status
from typing import List
from ..auth import oauth2
from ..schemas  import user_schema
from ..infra.sqlalchemy.config import database
from sqlalchemy.orm import Session
from ..infra.sqlalchemy.repository import user

get_db = database.get_db

router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post('/', response_model=user_schema.UserView, status_code=status.HTTP_201_CREATED)
def create_new_user(request: user_schema.UserBase, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/', status_code=200, response_model=List[user_schema.UserView])
def show_all_users(db: Session = Depends(get_db), current_user: user_schema.UserView = Depends(oauth2.get_current_user)):
    return user.show(db)

@router.get('/{id}', status_code=200, response_model= user_schema.UserView)
def show_user(id: str,db: Session = Depends(get_db)):
    return user.show_id(id, db)