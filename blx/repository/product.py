from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status, HTTPException, Depends

from uuid import uuid4

generate_uuid4 = str(uuid4())

def sell_new_product(request: schemas.Product, user_seller, db: Session):
    new_product = models.Product(   product_id = generate_uuid4,
                                    user_seller = user_seller,
                                    product_price = request.product_price,
                                    product_name = request.product_name,
                                    product_detail = request.product_detail,
                                    product_image = request.product_image,
                                    product_status = request.product_status,
                                    amount_of_product = request.amount_of_product)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def show_all_seller_products(db: Session):
    products = db.query(models.Product).all()
    return products

def show_seller_product_id(id: str, db: Session):
    product = db.query(models.Product).filter(models.Product.product_id == id).first()
    return product

def buy_product(request: schemas.ProductsSold, user_buyer_active, db: Session):

    product = db.query(models.Product).filter(models.Product.product_id == request.product_id).first()
    product_status = product.product_status
    amount_of_product = product.amount_of_product
    
    if amount_of_product == 0:
        product.product_status = False
        db.commit()

    if product_status and amount_of_product > 0:
        buy_new_product = models.ProductsSold(  products_sold_id = generate_uuid4,
                                                product_id = request.product_id,
                                                user_buyer_id = user_buyer_active)
        db.add(buy_new_product)
        product.amount_of_product = amount_of_product - 1
        db.commit()
        db.refresh(buy_new_product)
        return buy_new_product

    return {'data': 'Product Unavailable!'}

def show_sold_product_id(id: str, db: Session):
    sold_product = db.query(models.ProductsSold).filter(models.ProductsSold.product_id == id).first()
    return sold_product


def show_sold_products(db: Session):  
    products = db.query(models.ProductsSold).all()
    return products



