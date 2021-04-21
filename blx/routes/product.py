from fastapi import APIRouter, Depends, status
from .. import oauth2
from .. import schemas, models, database
from sqlalchemy.orm import Session
from typing import List
from ..repository import product


get_db = database.get_db

router = APIRouter(
    prefix='/product',
    tags=['Product']
)

@router.get('/soldProductsAll', status_code=200, response_model=List[schemas.SoldProductView])
async def show_all_sold_products(db: Session = Depends(get_db)):
    return product.show_sold_products(db)

@router.get('/soldProducts/{id}', status_code=200)
def show_sold_product_id(id, db: Session = Depends(get_db), current_user: schemas.UserView = Depends(oauth2.get_current_user)):
    return product.show_sold_product_id(id, db)

@router.get('/{id}',  status_code=200, response_model=schemas.ProductView)
def show_product(id, db: Session = Depends(get_db)):
    return product.show_seller_product_id(id, db)
    
@router.get('/', status_code=200)
def show_all_products(db: Session = Depends(get_db)):
    return product.show_all_seller_products(db)



@router.post ('/', status_code=status.HTTP_201_CREATED, response_model= schemas.ProductView)
def sell_product(request: schemas.Product, db: Session = Depends(get_db), current_user: schemas.UserView = Depends(oauth2.get_current_user)):
    return product.sell_new_product(request, current_user.user_id, db)

@router.post('/buy', status_code=status.HTTP_201_CREATED)
def buy_product(request: schemas.ProductsSold, db: Session = Depends(get_db), current_user: schemas.UserView = Depends(oauth2.get_current_user)):
    return product.buy_product(request, current_user.user_id, db)



