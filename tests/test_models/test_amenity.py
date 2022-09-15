#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity
import unittest
import inspect
import pep8 as pycodestyle
import models


class TestAmenityDocs(unittest.TestCase):
    """ Tests for documentation and styling of Amenity Class"""

    @classmethod
    def setUpClass(self):
        """setup for docstring tests"""
        self.base_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test to confirm that models/base_model.py conform to pep8"""
        for file in ['models/amenity.py',
                     'tests/test_models/test_amenity.py']:
            with self.subTest(path=file):
                errors = pycodestyle.Checker(file).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for pressence of module docstring"""
        self.assertTrue(len(models.amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_class_docstring(self):
        """Test for the presence of Amenity class docstring"""
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertTrue(
                    len(func.__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class test_Amenity(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
