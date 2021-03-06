#!/usr/bin/python3
"""
    Contains the BaseModel unittest.
"""
import os
import unittest
import models
from models.base_model import BaseModel


class TestBase_Model(unittest.TestCase):
    """Testing"""

    def test_docstring(self):
        """Test if functions, methods, classes
        and modules have docstring"""
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.base_model.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(BaseModel.__doc__, msj)  # Classes

    def test_executable_file(self):
        """Test if file has permissions u+x to execute"""
        # Check for read access
        is_read_true = os.access("models/base_model.py", os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access("models/base_model.py", os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access("models/base_model.py", os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_id(self):
        """Test if the id of two instances are different"""
        my_model = BaseModel()
        my_model1 = BaseModel()
        self.assertNotEqual(my_model.id, my_model1.id)

    def test_str(self):
        """Check if the output of str is in the specified format"""
        my_model4 = BaseModel()
        _dict = my_model4.__dict__
        string1 = "[BaseModel] ({}) {}".format(my_model4.id, _dict)
        string2 = str(my_model4)
        self.assertEqual(string1, string2)

    def test_save(self):
        """Check if the attribute updated_at (date) is updated for
        the same object with the current date"""
        my_model2 = BaseModel()
        first_updated = my_model2.updated_at
        my_model2.save()
        second_updated = my_model2.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """Check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format."""
        my_model3 = BaseModel()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == "created_at":
                self.assertIsInstance(value, str)
            if key == "updated_at":
                self.assertIsInstance(value, str)
