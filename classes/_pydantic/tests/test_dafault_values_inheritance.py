import unittest

from classes._pydantic import ChildInheritance, IntValueInheritance


class TestDefaultValuesPydanticInheritance(unittest.TestCase):
    def test_child_instance(self):
        child = ChildInheritance(a=1, b=IntValueInheritance(1), c=2)
        assert isinstance(child, ChildInheritance)

    def test_child_raise_error_when_b_is_default_zero(self):
        with self.assertRaises(ValueError):
            ChildInheritance(a=1, c=2)

    def test_child_raise_error_when_b_is_zero(self):
        with self.assertRaises(ValueError):
            ChildInheritance(a=1, b=IntValueInheritance(0), c=2)

    @unittest.skip("pydantic parse float as int")
    def test_child_raise_error_when_a_is_float(self):
        with self.assertRaises(TypeError):
            ChildInheritance(a=1.0, b=1, c=2)  # type: ignore
