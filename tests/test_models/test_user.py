#!/usr/bin/python3
""" Contains unittests for User class """
import unittest
import os
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """ Tests User class """

    def test_class(self):
        """ tests class instantiation and class attributes """
        # create object instance of User Class
        obj = User()
        # check if object is an instance of User and parent class
        self.assertIsInstance(obj, User)
        self.assertIsInstance(obj, BaseModel)
        # check if dictionaries contain all expected attributes
        # __dict__ only contains set attributes so this checks if set
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("email", User.__dict__)
        self.assertIn("password", User.__dict__)
        self.assertIn("first_name", User.__dict__)
        self.assertIn("last_name", User.__dict__)
        # check if User class attributes initialized correctly
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")
