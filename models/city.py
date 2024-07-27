#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, MetaData, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship('State', back_populates='cities')
    __table_args__ = (
        {'foreign_keys': [state_id]},
    )