from pydantic import BaseModel
from typing import List
from . import product_schema

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
    products: List[product_schema.ProductView]
    
    class Config():
        orm_mode = True

class BuyerUserView(BaseModel):
    user_name: str
    user_phone: str
    user_address: str
   
    class Config():
        orm_mode = True