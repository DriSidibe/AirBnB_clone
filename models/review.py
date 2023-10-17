#!/usr/bin/env python3
from .base_model import BaseModel

"""
    the review package
"""


class Review(BaseModel):
    """ the Review class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
