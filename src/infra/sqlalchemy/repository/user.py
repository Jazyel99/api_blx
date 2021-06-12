from sqlalchemy.orm import Session
from ..models import models
from ....schemas import user_schema
from ....auth.hashing import Hash
from fastapi import status, HTTPException
from uuid import uuid4

generate_uuid4 = str(uuid4())

def create(request: user_schema.UserBase, db: Session):
    new_user = models.User( user_id = generate_uuid4,
                            user_name = request.user_name,
                            user_phone = request.user_phone,
                            user_address = request.user_address,
                            user_password = Hash.bcrypt(request.user_password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(db: Session):
    users = db.query(models.User).all()
    return users

def show_id(id: str, db: Session):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id \'{id}\' is not available')
    return user
