#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Class City for our sql table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto", unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
