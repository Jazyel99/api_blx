from fastapi import APIRouter, Depends, status
from ..auth import oauth2
from ..schemas import user_schema, product_schema
from ..infra.sqlalchemy.config import database
from sqlalchemy.orm import Session
from typing import List
from ..infra.sqlalchemy.repository import product


get_db = database.get_db

router = APIRouter(
    prefix='/product',
    tags=['Product']
)

@router.get('/myProducts', status_code=200, response_model=List[product_schema.ProductSimpleView])
def my_products(db: Session = Depends(get_db), current_user: user_schema.UserView = Depends(oauth2.get_current_user)):
    return product.show_my_products(db, current_user.user_id)

#visualizar as compras realizados pelo usuário logado
@router.get('/purchasedProducts', status_code=200)
def show_purchased_products(db: Session = Depends(get_db), current_user: user_schema.UserView = Depends(oauth2.get_current_user)):
    return product.show_purchased_products(db, current_user.user_id)

#rota responsavel postar um novo produto a ser vendido
@router.post ('/', status_code=status.HTTP_201_CREATED, response_model= product_schema.ProductView)
def sell_product(request: product_schema.Product, db: Session = Depends(get_db), current_user: user_schema.UserView = Depends(oauth2.get_current_user)):
    return product.sell_new_product(request, current_user.user_id, db)

#rota responsavel por ralizar a compra de produto
@router.post('/buy/{product_id}/{amount_product}', status_code=status.HTTP_201_CREATED)
def buy_product(product_id, amount_product:int, db: Session = Depends(get_db), current_user: user_schema.UserView = Depends(oauth2.get_current_user)):
    return product.buy_product(product_id, amount_product, current_user.user_id, db)

#rota responsavel pela atualização de atributos de produto
@router.put('/editProduct/{product_id}')
def edit_product(product_id, request: product_schema.Product, current_user: user_schema.UserView = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return product.edit_products(request, current_user.user_id, product_id, db)

#remover produto
@router.delete('/delete_product/{product_id}')
def delete(product_id, current_user: user_schema.UserView = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return product.delete_product(product_id, current_user.user_id, db)