from fastapi import APIRouter, Depends, status
from ..auth import oauth2
from ..schemas import user_schema, product_schema
from ..infra.sqlalchemy.config import database
from sqlalchemy.orm import Session
from typing import List
from ..infra.sqlalchemy.repository import product_for_sale

get_db = database.get_db

router = APIRouter(
    prefix='/product',
    tags=['Product for sale']
)

@router.get('/soldProductsAll', status_code=200, response_model=List[product_schema.ProductView])
async def show_all_sold_products(db: Session = Depends(get_db), current_user: user_schema.UserView = Depends(oauth2.get_current_user)):
    return product_for_sale.show_products_for_sale(db, current_user.user_id)