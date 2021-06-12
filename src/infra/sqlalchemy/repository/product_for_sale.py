from sqlalchemy.orm import Session
from ..models import models
from .... import schemas
from fastapi import status, HTTPException, Depends

#mostrar todos os produtos que estão à venda
def show_products_for_sale(db: Session, user_active):
    products = db.query(models.Product).filter(models.Product.user_seller != user_active).all()
    return products
