# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy import select

from app.db import db
from app.models import User

from app.auth.jwt import create_access_token, get_current_user
from app.auth import schema

router = APIRouter(tags=['auth'])


@router.post('/api/auth/login', response_model=schema.LoginResponse)
def login(request: schema.LoginRequest):
    with db.Session() as session:
        user = session.execute(
            select(User).filter_by(email=request.email)
        ).scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid Credentials'
        )

    if not user.check_password(request.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid Password'
        )

    # Generate a JWT Token
    access_token = create_access_token(data={'sub': user.email})

    return {
        'token': {
            'access_token': access_token,
            'token_type': 'bearer',
        },
        'user': {
            'id': user.id,
            'email': user.email,
            'is_superuser': user.is_superuser,
            'is_admin': user.is_admin
        }
    }

# How to use JWT authorization:
# @router.get('/api/users/me', response_model=schema.TokenData)
# def get_me(current_user: User = Depends(get_current_user)):
#     return current_user
