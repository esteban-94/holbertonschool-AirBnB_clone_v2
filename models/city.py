#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "cities"
        name = Column(String(128))
        state_id = Column(String(60), ForeignKey("State.id"))
    else:
        state_id = ""
        name = ""
