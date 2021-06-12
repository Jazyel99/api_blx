from sqlalchemy.orm import Session
from ..models import models
from ....schemas import user_schema, product_schema
from fastapi import status, HTTPException, Depends

from uuid import uuid4

generate_uuid4 = str(uuid4())

#visualizar todos os productos do usuário que está logado
def show_my_products(db: Session, user_active):
    products = db.query(models.Product).filter(models.Product.user_seller == user_active).all()
    return products

#visualizar as compras realizados pelo usuário logado
def show_purchased_products(db: Session, user_active):
    purchased_products = db.query(models.ProductOrder).filter(models.ProductOrder.user_buyer_id == user_active).all()
    return purchased_products

def sell_new_product(request: product_schema.Product, user_seller, db: Session):
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

#comprar produto
def buy_product(product_id, the_amount, user_buyer_active, db: Session):
    #Se o ID do request for igual a algum exitente na tabela
    #Ira retornar o produto a ser comprado
    product = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    product_status = product.product_status
    amount_of_product = product.amount_of_product
    
    #se quantide for igual a zero
    #Atribuir ao status do produto o valor False
    if amount_of_product == 0:
        product.product_status = False
        db.commit()

    #se o status do produto for verdadeiro e quantidade de produto for maior que 0
    #Então temos produto disponível para a compra
    if product_status and amount_of_product > 0:
        #Atribuido um ID que identifica  o produto
        #Atrubuido o id do produto que foi comprado
        #Atribindo o id do usário comprador
        buy_new_product = models.ProductOrder(  product_id = product_id,
                                                user_buyer_id = user_buyer_active,
                                                amount_product = the_amount)
        #adicionado na tabelda de produtos comprados
        db.add(buy_new_product)
        #Decrementado a quantidade de produtos do produto comprado
        #E atualizado-o no Bando de dados
        product.amount_of_product = amount_of_product - the_amount
        db.commit()
        db.refresh(buy_new_product)

        return buy_new_product


    return {'data': 'Product Unavailable!'}

# O usuário poderá editar somente seus produtos
def edit_products(request, user_id, product_id, db:Session):
    product = db.query(models.Product).filter(models.Product.product_id == product_id, models.Product.user_seller == user_id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Product with id {product_id} not found')
    product.update(request.dict())
    db.commit()
    return request

#deletando produto do usuário logado
def delete_product(product_id, user_active, db:Session):
    product = db.query(models.Product).filter(models.Product.product_id == product_id, models.Product.user_seller == user_active)

    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Product with id {product_id} not found')
    db.delete(product.first())
    db.commit()
    return 'deleted'



