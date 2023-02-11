#!/usr/bin/python3
""" Contains unittests for BaseModel class """
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelClass(unittest.TestCase):
    """ Tests BaseModel class """

    def test_init(self):
        """ Tests init method """
        # create object instance of BaseModel class
        obj = BaseModel()
        # check if object is an instance of BaseModel
        self.assertIsInstance(obj, BaseModel)
        # check if dictionary contains all expected attributes
        # __dict__ only contains set attributes so this checks if set
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        # check if public instance attributes are of correct type
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        # create dictionary to set obj values to with **kwargs
        new_dict = {}
        new_dict["id"] = "012345"
        new_dict["created_at"] = "1995-2-2T10:23:35.123450"
        new_dict["updated_at"] = "1999-1-4T7:15:05.543210"
        # create object instance with **kwargs and run similar testing
        obj2 = BaseModel(**new_dict)
        self.assertIsInstance(obj2, BaseModel)
        self.assertIn("id", obj2.__dict__)
        self.assertIn("created_at", obj2.__dict__)
        self.assertIn("updated_at", obj2.__dict__)
        self.assertIsInstance(obj2.id, str)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsInstance(obj2.updated_at, datetime)
        # can also test exact values, including formatting of datetimes
        self.assertEqual(obj2.id, "012345")
        string = "1995-02-02 10:23:35.123450"
        self.assertEqual("{}".format(obj2.created_at), string)
        string = "1999-01-04 07:15:05.543210"
        self.assertEqual("{}".format(obj2.updated_at), string)

    def test_str(self):
        """ Tests __str__ method """
        obj = BaseModel()
        cls = type(obj).__name__
        string = "[{}] ({}) {}".format(cls, obj.id, obj.__dict__)
        # check if __str__ returns expected string representation
        self.assertEqual(obj.__str__(), string)

    def test_save(self):
        """ Tests save method """
        obj = BaseModel()
        # test that update_at changes by holding values before and after save
        a = obj.updated_at
        obj.save()
        b = obj.updated_at
        self.assertNotEqual(a, b)

    def test_to_dict(self):
        """ Tests to_dict method """
        obj = BaseModel()
        dict_rep = obj.to_dict()
        # check if all keys from obj.__dict__ and __class__ in dict_rep
        for key in obj.__dict__:
            self.assertIn("{}".format(key), dict_rep)
        self.assertIn("__class__", dict_rep)
        # check if dictionary values are correct type
        self.assertIsInstance(dict_rep["id"], str)
        self.assertIsInstance(dict_rep["created_at"], str)
        self.assertIsInstance(dict_rep["updated_at"], str)
        self.assertIsInstance(dict_rep["__class__"], str)
        # check if dictionary values are correct
        self.assertEqual(dict_rep["id"], obj.id)
        self.assertEqual(dict_rep["__class__"], type(obj).__name__)
        string = str(datetime.isoformat(obj.created_at))
        self.assertEqual(dict_rep["created_at"], string)
        string = str(datetime.isoformat(obj.updated_at))
        self.assertEqual(dict_rep["updated_at"], string)
        # check if new instance can be created with to_dict as kwargs
        obj2 = BaseModel(**dict_rep)
        # check if created new instance and set all attributes
        self.assertIsInstance(obj2, BaseModel)
        self.assertIn("id", obj2.__dict__)
        self.assertIn("created_at", obj2.__dict__)
        self.assertIn("updated_at", obj2.__dict__)
        # check if attributes correct type and same value as original
        self.assertIsInstance(obj2.id, str)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsInstance(obj2.updated_at, datetime)
        self.assertEqual(obj2.id, obj.id)
        self.assertEqual(obj2.created_at, obj.created_at)
        self.assertEqual(obj2.updated_at, obj.updated_at)
        self.assertEqual(type(obj2).__name__, type(obj).__name__)
        # check that new object is a different instance
        self.assertIsNot(obj, obj2)
