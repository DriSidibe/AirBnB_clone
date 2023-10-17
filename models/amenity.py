#!/usr/bin/env python3
from .base_model import BaseModel

"""
    the Amenity package
"""


class Amenity(BaseModel):
    """ the Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
