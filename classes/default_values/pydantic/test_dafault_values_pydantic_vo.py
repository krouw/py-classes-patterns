import unittest

from classes.default_values.pydantic import ChildVO, IntValueVO


class TestDefaultValuesPydanticVO(unittest.TestCase):
    def test_child_instance(self):
        child = ChildVO(a=1, b=IntValueVO(value=1), c=2)
        assert isinstance(child, ChildVO)

    @unittest.skip("Cannot be Implement")
    def test_child_raise_error_when_b_is_default_zero(self):
        with self.assertRaises(ValueError):
            ChildVO(a=1, c=2)

    def test_child_raise_error_when_b_is_zero(self):
        with self.assertRaises(ValueError):
            ChildVO(a=1, b=IntValueVO(value=0), c=2)

    @unittest.skip("pydantic parse float as int")
    def test_child_raise_error_when_a_is_float(self):
        with self.assertRaises(TypeError):
            ChildVO(a=1.0, b=IntValueVO(value=1), c=2)
