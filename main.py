from fastapi import FastAPI
from src.infra.sqlalchemy.models import models
from src.infra.sqlalchemy.config.database import Base, engine
from src.routes import user, product, authentication, product_order, products_for_sale
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(products_for_sale.router)
app.include_router(product_order.router)
