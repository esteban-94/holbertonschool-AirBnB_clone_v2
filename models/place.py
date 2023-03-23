""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import *
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv
metadata = Base.metadata()


class Place(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') == "db":
        place_amenity = Table("place_amenity", metadata,
                                Column("place_id", String(60),
                                        ForeignKey("places.id"),
                                        primary_key=True),
                                Column("amenity_id", String(60),
                                        ForeignKey("amenities.id"),
                                        primary_key=True))

        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        name = Column(String(128))
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                            backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                viewonly=False, backref="places",
                                cascade='all, delete, delete-orphan')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def reviews(self):
            new_list = []
            for value in models.storage.all(Review).values():
                if value.place_id == self.place_id:
                    new_list.append(value)
            return new_list

        @property
        def amenities(self):
            new_list = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    new_list.append(amenity)
            return new_list
