#!/usr/bin/python3
"""
Contains the test suites for BaseModel class
python3 -m unittest tests/test_models/test_base_model.py
"""

from datetime import datetime
import os
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

    def test_automatic_id_and_dates_generation(self):
        """
        Checks if the id, created_at and updated_at are
        automatically generated if they are not in kwargs
        """
        my_dictionary = {}
        obj = BaseModel(**my_dictionary)
        self.assertTrue(type(obj.id) is str)
        self.assertTrue(type(obj.created_at) is datetime)
        self.assertTrue(type(obj.updated_at) is datetime)

    def test_generation_from_kwargs(self):
        """
        Tests if properties are really passed from kwargs
        """
        temp_date = datetime.now()
        tmp_date_iso = temp_date.isoformat()
        obj = BaseModel(id="382", created_at=tmp_date_iso, name="Jay")
        self.assertEqual(obj.id, "382")
        self.assertEqual(obj.created_at, temp_date)
        self.assertEqual(obj.name, "Jay")

    def test_args_are_ignored(self):
        """
        Tests whether args will be ignored and kwargs taken in
        """
        obj = BaseModel("342", id="738902367")
        self.assertEqual(obj.id, "738902367")

    def test_args_unused(self):
        """
        Arguements not used
        """
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_two_models_different_updated_at(self):
        """
        different update times
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertLess(obj1.updated_at, obj2.updated_at)

    def test_two_models_different_created_at(self):
        """
        Models should have different created at
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_no_args_instantiates(self):
        """
        Even if there are no args, instantiation should still be possible
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_that_to_dict_contains_correct_keys(self):
        """
        Checks whether to_dict() returns the expected key
        """
        obj_dict = BaseModel().to_dict()
        attrs = ("id", "created_at", "updated_at", "__class__")
        for attr in attrs:
            self.assertIn(attr, obj_dict)

    def test_instantiation_with_None_kwargs(self):
        """
        Tests instantiation with none kwargs
        """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_to_dict_not_dunder_dict(self):
        """Checks that to_dict() is a dict object not equal to __dict__"""
        obj = BaseModel()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_output(self):
        """
        Samples the dictionary output against expected output
        """
        dt = datetime.today()
        obj = BaseModel()
        obj.id = "123456"
        obj.created_at = obj.updated_at = dt
        test_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(obj.to_dict(), test_dict)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        """
        Ran before this test suite is started
        """
        try:
            os.rename("file.json", "tmp_file")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """
        Ran after this test suite is finished
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp_file", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """
        Tests one save to a file
        """
        bm = BaseModel()
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        """
        Tests two saves to a file
        """
        obj = BaseModel()
        first_updated_at = obj.updated_at
        obj.save()
        second_updated_at = obj.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        obj.save()
        self.assertLess(second_updated_at, obj.updated_at)

    def test_save_with_arg(self):
        """
        Simply tests saving with args
        """
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        """
        Checks if the save method indeed updates a file
        """
        obj = BaseModel()
        obj.save()
        objid = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(objid, f.read())

    def test_save_updates_file_2(self):
        """
        Checks if the save method updates a file
        """
        obj = BaseModel()
        obj.save()
        objid = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(objid, f.read())

    def test_save_update_file(self):
        """
        Tests if file is updated when the 'save' is called
        """
        obj = BaseModel()
        obj.save()
        objid = "BaseModel.{}".format(obj.id)
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(objid, f.read())


if __name__ == "__main__":
    unittest.main()
