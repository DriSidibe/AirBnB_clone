#!/usr/bin/python3
""" Contains unittests for City class """
import unittest
import os
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """ Tests City class """

    def test_class(self):
        """ tests class instantiation and class attributes """
        # create object instance of City Class
        obj = City()
        # check if object is an instance of City and parent class
        self.assertIsInstance(obj, City)
        self.assertIsInstance(obj, BaseModel)
        # check if dictionaries contain all expected attributes
        # __dict__ only contains set attributes so this checks if set
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", City.__dict__)
        self.assertIn("state_id", City.__dict__)
        # check if City class attribute initialized correctly
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.state_id, "")
