#!/usr/bin/python3
""" Module that create and manages the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class """
    name = ""
    state_id = ""
