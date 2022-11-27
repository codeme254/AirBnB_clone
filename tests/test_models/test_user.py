#!/usr/bin/python3
"""
Test suite for the User class in models.user
python3 -m unittest tests/test_models/test_user.py
"""
import unittest
from models.base_model import BaseModel

from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def test_attrs_are_class_attrs(self):
        """
        Tests if the attributes are class attributes
        """
        u = User()
        # test that it is a class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_class_attrs(self):
        """
        Tests all the class attributes
        """
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        """
        Tests that user class is a child of BaseModel class
        """
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))

    def test_to_dict_type(self):
        """
        Tests to_dict method of BaseClass in User class
        """
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """
        Ensures to_dict for User class contains correct keys
        """
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """
        Tests to_dict contains added attributes
        """
        us = User()
        us.middle_name = "Holberton"
        us.my_number = 98
        self.assertEqual("Holberton", us.middle_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """
        Tests to_dict datetime attributes are of str data type
        """
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        """
        Tests to_dict output for User class
        """
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """
        Contrasting to_dict with dunder dict
        """
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        """
        Tests to_dict with arguements
        """
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)
