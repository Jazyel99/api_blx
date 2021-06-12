from fastapi import APIRouter, Depends, status
from ..auth import oauth2
from ..schemas import user_schema
from ..infra.sqlalchemy.config import database
from ..infra.sqlalchemy.models import models
from sqlalchemy.orm import Session
from typing import List
from ..infra.sqlalchemy.repository import product_order

get_db = database.get_db

router = APIRouter(
    prefix='/product',
    tags=['Product Order']
)

#mostar pedidos
@router.get('/product_order', status_code=200)
def show_product_order(current_user: user_schema.UserView = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return product_order.show_product_order(db, current_user.user_id)