#!/usr/bin/python3
""" Contains unittests for State class """
import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    """ Tests State class """

    def test_class(self):
        """ tests class instantiation and class attributes """
        # create object instance of State Class
        obj = State()
        # check if object is an instance of State and parent class
        self.assertIsInstance(obj, State)
        self.assertIsInstance(obj, BaseModel)
        # check if dictionaries contain all expected attributes
        # __dict__ only contains set attributes so this checks if set
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", State.__dict__)
        # check if State class attribute initialized correctly
        self.assertEqual(State.name, "")
        self.assertEqual(obj.name, "")
