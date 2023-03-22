#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class User(BaseModel):
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "users"
        email = Column(String(128))
        password = Column(String(128))
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
