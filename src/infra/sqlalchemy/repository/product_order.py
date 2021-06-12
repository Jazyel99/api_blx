from sqlalchemy.orm import Session
from ..models import models
from .... import schemas
from fastapi import status, HTTPException, Depends

#mostar todos os pedidos
def show_product_order(db: Session, user_active):  
    products = db.query(models.ProductOrder).filter(models.ProductOrder.user_buyer_id != user_active).all()
    return products