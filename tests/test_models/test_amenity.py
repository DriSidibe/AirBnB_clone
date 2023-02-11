#!/usr/bin/python3
""" Contains unittests for Amenity class """
import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """ Tests Amenity class """

    def test_class(self):
        """ tests class instantiation and class attributes """
        # create object instance of Amenity Class
        obj = Amenity()
        # check if object is an instance of Amenity and parent class
        self.assertIsInstance(obj, Amenity)
        self.assertIsInstance(obj, BaseModel)
        # check if dictionaries contain all expected attributes
        # __dict__ only contains set attributes so this checks if set
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", Amenity.__dict__)
        # check if Amenity class attribute initialized correctly
        self.assertEqual(Amenity.name, "")
        self.assertEqual(obj.name, "")
