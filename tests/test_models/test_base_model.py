#!/usr/bin/python3
"""
Contains the test suites for BaseModel class
"""

from datetime import datetime
import unittest

import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel
    """

    def test_if_basemodel_instance_has_id(self):
        """
        Tests if base model instance has an id
        """
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))

    def test_str_representation(self):
        """
        Checks if the string repesentation is appropriate
        """
        obj = BaseModel()
        self.assertEqual(str(obj),
                         "[BaseModel] ({}) {}".format(obj.id, obj.__dict__))

    def test_ids_are_unique(self):
        """
        Tests if IDs generated are unique
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_type_of_id_is_string(self):
        """
        Checks if the data type of id is string
        """
        obj = BaseModel()
        self.assertTrue(type(obj.id) is str)

    def test_updated_is_datetime(self):
        """
        Checks if the updated_at attribute is datetime object
        """
        obj = BaseModel()
        self.assertTrue(type(obj.updated_at) is datetime)

    def test_created_is_datetime(self):
        """
        Checks if the updated_at attribute is datetime object
        """
        obj = BaseModel()
        self.assertTrue(type(obj.created_at) is datetime)

    def test_created_at_eq_updated_at_initially(self):
        """
        Asserts that initially, created == updated initially
        """
        obj = BaseModel()
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_to_dict_returns_a_dictionary(self):
        """
        Tests if to_dict method inddeed returns a dictionary
        """
        obj = BaseModel()
        self.assertTrue(type(obj.to_dict()) is dict)


if __name__ == "__main__":
    unittest.main()
