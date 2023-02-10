#!/usr/bin/env python3
from .base_model import BaseModel

"""
    the state package
"""


class State(BaseModel):
    """ the State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
