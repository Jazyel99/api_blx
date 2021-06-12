from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
#from .database import Base
from ..config.database import Base


class User(Base):
    __tablename__ = "users"
    
    user_id = Column(String, primary_key=True,)
    user_name = Column(String)
    user_phone = Column(String, unique= True)
    user_address = Column(String)
    user_password = Column(String)
    
    products = relationship("Product", back_populates="user_id_seller")
 
class Product(Base):
    __tablename__ = "products"
    
    product_id = Column(String, primary_key=True, index=True)
    user_seller = Column(String, ForeignKey('users.user_id'))
    product_price = Column(Float)
    product_name = Column(String)
    product_detail = Column(String)
    product_image = Column(String)
    product_status = Column(Boolean)
    amount_of_product = Column(Integer)

    user_id_seller = relationship("User", back_populates="products")

#tabela de pedidos
class ProductOrder(Base):
    __tablename__ = "product_order"
    
    product_order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(String, ForeignKey('products.product_id'))
    user_buyer_id = Column(String, ForeignKey('users.user_id'))
    amount_product = Column(Integer)
    
    buyer_user = relationship('User')
    purchased_product = relationship('Product')