#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    __table_args__ = (
    {'mysql_default_charset': 'latin1'}
)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        from models import storage

        def cities(self):
            return storage.cities(self)
