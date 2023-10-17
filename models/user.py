#!/usr/bin/env python3
from .base_model import BaseModel

"""
    the User package
"""


class User(BaseModel):
    """ the User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
