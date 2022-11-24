#!/usr/bin/env python3
"""
Contains test suites for the base model class
Run this file at the root of the project directory with the comand:
python3 -m unittest -v tests/test_models/test_base_model.py
"""
# Run this file at the root of the project directory using this command
# python3 -m unittest  tests/test_models/test_base_model.py

from datetime import datetime
import unittest
from uuid import uuid4

import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests the base model to ensure all is running ok
    """

    def test_if_base_model_instance_has_id(self):
        """
        Checks if any instance of a base model has an id
        """
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))

    def test_str_representation(self):
        """
        Tests if the string representation is ok
        """

        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_unique_id(self):
        """
        Tests if ids generated are unique
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id, obj3.id)

    def test_id_type_is_str(self):
        """
        Checks if the id of any instance is a string
        """
        b = BaseModel()
        self.assertTrue(type(b.id) == str)

    def test_created_at_is_datetime(self):
        """
        Checks if the created_at property is f datetime data type
        """
        obj = BaseModel()
        self.assertTrue(type(obj.created_at) == datetime)

    def test_updated_at_is_datetime(self):
        """
        Tests if updated at property is of datetime data type
        """
        obj = BaseModel()
        self.assertTrue(type(obj.updated_at) == datetime)

    def test_two_instances_have_different_created_at(self):
        """
        Checks if two instances have a different created at value
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_created_at_and_updated_at_initially_equal(self):
        """
        Initially, created at and updated at are supposed to be equal
        This test tests just that
        """
        obj = BaseModel()
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_save_method_updates_updated_at_attribute(self):
        """
        Checks if the save method updates the updated at attribute
        """
        obj = BaseModel()
        current_updated_time = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, current_updated_time)

    def test_if_to_dict_returns_a_dictionary(self):
        """
        Tests if to_dict method really returns a dictionary
        """
        obj = BaseModel()
        self.assertTrue(type(obj.to_dict()) == dict)

    def test_if_dict_has_class_magic_method(self):
        """
        tests if __class__ is available in dict of an instance of Basemodel
        """
        obj = BaseModel()
        self.assertTrue("__class__" in obj.to_dict())

    def test_if_created_at_returned_by_dict_is_an_iso_string(self):
        """
        tests if created at property returned by to_dict is an iso string
        """
        obj = BaseModel()
        created_at_iso = obj.created_at.isoformat()
        self.assertEqual(obj.to_dict()["created_at"], created_at_iso)

    def test_if_updated_at_returned_by_dict_ia_an_iso_string(self):
        """
        Tests if updated at property returned by to_dict is an iso string
        """
        obj = BaseModel()
        updated_at_iso = obj.updated_at.isoformat()
        self.assertEqual(obj.to_dict()["updated_at"], updated_at_iso)

    def test__id_created_updated_auto_generated_if_kwargs__empty(self):
        """
        Checks that id, created at and updated at are automatically generated
        If Kwargs is empty
        """
        kwargs = {}
        obj = BaseModel(**kwargs)
        self.assertTrue(type(obj.id) == str)
        self.assertTrue(type(obj.created_at) is datetime)
        self.assertTrue(type(obj.updated_at) is datetime)

    def test_id_created_updated_generated_from_kwargs_if_kwargs_(self):
        """
        tests whether id, created at and updated at are generated
        from kwargs if kwargs is passed
        """
        obj_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                    "updated_at": datetime.utcnow().isoformat()}
        obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, obj_dict["id"])
        self.assertEqual(obj.created_at,
                         datetime.strptime(obj_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(obj.updated_at,
                         datetime.strptime(obj_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_when_args_and_kwargs_are_passed(self):
        """
        When args and kwargs are passed, BaseModel should ignore args
        """
        dt = datetime.now()
        dt_iso = dt.isoformat()
        b = BaseModel("4234", id="2344", created_at=dt_iso, name="some name")
        self.assertEqual(b.id, "2344")
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.name, "some name")

    def test_save_method_updates_updated_at_attr(self):
        """
        Checks that the save method updates the updated at attribute
        """
        obj = BaseModel()
        old_update_time = obj.updated_at
        obj.save()
        new_update_time = obj.updated_at
        self.assertLess(old_update_time, new_update_time)


if __name__ == "__main__":
    unittest.main()
