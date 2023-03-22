#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

storage_engine = getenv("HBNB_TYPE_STORAGE")

if storage_engine == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""  
        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    t_format = '%Y-%m-%dT%H:%M:%S.%f'
                    self.__dict__[k] = datetime.strptime(v, t_format)
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = self.__class__.__name__
        return f'[{cls}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        for key in dictionary.keys():
            if key == "_sa_instance_state":
                dictionary.pop(key)
        return dictionary
    
    def delete(self):
      """Dete the current intance from the storage"""
      models.storage.delete(self)
