from pydantic import BaseModel
from typing import Optional, List

class Product(BaseModel):
    product_name: str
    product_price: float
    product_detail: str
    product_image: str
    product_status: bool
    amount_of_product: int

class ProductView(Product):
    product_id: str
    product_name: str
    product_price: float
    product_detail: str
    product_image: str
    product_status: str
    amount_of_product: int
    
    class Config():
        orm_mode = True

class UserBase(BaseModel):
    user_name: str
    user_phone: str
    user_address: str
    user_password: str

class UserView(BaseModel):
    user_id: str
    user_name: str
    user_phone: str
    user_address: str
    products: List[ProductView]
    
    
    class Config():
        orm_mode = True

class BuyerUserView(BaseModel):
    user_name: str
    user_phone: str
    user_address: str
    class Config():
        orm_mode = True

class ProductsSold(BaseModel):
    product_id: str

class SoldProductView(BaseModel):
    products_sold_id: str
    buyer_user: BuyerUserView
    purchased_product: ProductView
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    user_id: Optional[str] = None