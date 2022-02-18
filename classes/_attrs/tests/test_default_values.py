import unittest

from classes._attrs import Child


class TestDefaultValuesAttrs(unittest.TestCase):
    def test_child_instance(self):
        child = Child(a=1, b=1, c=2)
        assert isinstance(child, Child)

    def test_child_raise_error_when_b_is_default_zero(self):
        with self.assertRaises(ValueError):
            Child(a=1, c=2)

    def test_child_raise_error_when_b_is_zero(self):
        with self.assertRaises(ValueError):
            Child(a=1, b=0, c=2)

    def test_child_raise_error_when_a_is_float(self):
        with self.assertRaises(TypeError):
            Child(a=1.0, b=1, c=2)  # type: ignore
