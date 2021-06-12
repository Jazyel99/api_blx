from pydantic import BaseModel

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

class ProductSimpleView(BaseModel):
    product_name: str
    product_price: float
    product_detail: str
    
    class Config():
        orm_mode = True