#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from city import City
from os import getenv
import models

class State(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                            backref="state")
    else:
        @property
        def cities(self):
            new_list = []
            for value in models.storage.all(City).values():
                if value.state_id == self.state_id:
                    new_list.append(value)
            return new_list
