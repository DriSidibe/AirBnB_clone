#!/usr/bin/env python3
from ..base_model import BaseModel
from ..user import User
from ..place import Place
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..review import Review

knowns_obj = {"BaseModel": BaseModel,
              "User": User,
              "Place": Place,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Review": Review}
