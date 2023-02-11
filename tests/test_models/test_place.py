#!/usr/bin/python3
""" Contains unittests for Place class """
import unittest
import os
from models.base_model import BaseModel
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """ Tests Place class """

    def test_class(self):
        """ tests class instantiation and class attributes """
        # create object instance of Place Class
        obj = Place()
        # check if object is an instance of Place and parent class
        self.assertIsInstance(obj, Place)
        self.assertIsInstance(obj, BaseModel)
        # check if dictionaries contain all expected attributes
        # __dict__ only contains set attributes so this checks if set
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("city_id", Place.__dict__)
        self.assertIn("user_id", Place.__dict__)
        self.assertIn("name", Place.__dict__)
        self.assertIn("description", Place.__dict__)
        self.assertIn("number_rooms", Place.__dict__)
        self.assertIn("number_bathrooms", Place.__dict__)
        self.assertIn("max_guest", Place.__dict__)
        self.assertIn("price_by_night", Place.__dict__)
        self.assertIn("latitude", Place.__dict__)
        self.assertIn("longitude", Place.__dict__)
        self.assertIn("amenity_ids", Place.__dict__)
        # check if Place class attribute initialized correctly
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])
