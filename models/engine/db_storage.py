#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
MYSQL_USER = getenv('HBNB_MYSQL_USER')
MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
MYSQL_DB = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(MYSQL_USER,
                                              MYSQL_PWD,
                                              MYSQL_HOST,
                                              MYSQL_DB))
        hbnb_env = getenv("HBNB_ENV")
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        pass

    def add(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        pass
    
