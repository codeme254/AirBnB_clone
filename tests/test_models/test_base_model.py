#!/usr/bin/python3
"""
Contains the test suites for BaseModel class
python3 -m unittest tests/test_models/test_base_model.py
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

    def test_two_models_different_created_at(self):
        """
        Checks that the attribute 'created_at' of 2 models are different
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_that_save_func_update_update_at_attr(self):
        """
        Checks that save() method updates the updated_at attribute
        """
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)
        self.assertGreater(b.updated_at.microsecond,
                           b.created_at.microsecond)

    def test_if_to_dict_returns_class_dunder_method(self):
        """
        Checks if BaseModel.to_dict() contains __class__
        """
        b = BaseModel()
        self.assertTrue("__class__" in b.to_dict())

    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
        """
        Checks that created_at is stored as a str obj in ISO format
        """
        b = BaseModel()
        self.assertEqual(b.to_dict()["created_at"], b.created_at.isoformat())

    def test_that_updated_at_returned_by_to_dict_is_an_iso_string(self):
        """
        Checks that updated_at is stored as a str obj in ISO format
        """
        b = BaseModel()
        self.assertEqual(b.to_dict()["updated_at"], b.updated_at.isoformat())

    def test_if_to_dict_returns_the_accurate_number_of_keys(self):
        """
        Checks that to_dict() returns the expected number of keys/values
        """
        b = BaseModel()
        partial_expectation = {k: v for k, v in b.__dict__.items()
                               if not k.startswith("_")}
        self.assertEqual(len(b.to_dict()), len(partial_expectation) + 1)


if __name__ == "__main__":
    unittest.main()
