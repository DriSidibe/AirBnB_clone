#!/usr/bin/python3
""" Contains unittests for Review class """
import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """ Tests Review class """

    def test_class(self):
        """ tests class instantiation and class attributes """
        # create object instance of Review Class
        obj = Review()
        # check if object is an instance of Review and parent class
        self.assertIsInstance(obj, Review)
        self.assertIsInstance(obj, BaseModel)
        # check if dictionaries contain all expected attributes
        # __dict__ only contains set attributes so this checks if set
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("place_id", Review.__dict__)
        self.assertIn("user_id", Review.__dict__)
        self.assertIn("text", Review.__dict__)
        # check if Review class attribute initialized correctly
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")
