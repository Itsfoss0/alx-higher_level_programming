#!/usr/bin/python
"""
City Model definition. Defines the city class
Inheriting from the Base model which is defined
in the model_state model
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City:
    """
    id (int):  city id
    name (str): City name
    state_id(int): ID of the state to which this city belongs
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
