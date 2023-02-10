#!/usr/bin/env python3
from .base_model import BaseModel

"""
    the city package
"""


class City(BaseModel):
    """ the City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
