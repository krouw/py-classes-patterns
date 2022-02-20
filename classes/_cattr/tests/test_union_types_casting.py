import unittest

from classes._cattr import (
    TypeA,
    TypeA1,
    TypeA2,
    TypeA3,
    TypeB,
    TypeB1,
    TypeB2,
    TypeB3,
)


class TestUnionTypesCastingCattrA(unittest.TestCase):
    def test_type_a(self):
        type_a_1 = TypeA1(a1=1)
        type_a_2 = TypeA2(a1=1.0, a2=True)
        type_a_3 = TypeA3(a1=1.0, a2=True, a3=1)
        type_a1 = TypeA(value=type_a_1)
        assert isinstance(type_a1, TypeA)
        assert isinstance(type_a1.value, TypeA1)
        type_a2 = TypeA(value=type_a_2)
        assert isinstance(type_a2, TypeA)
        assert isinstance(type_a2.value, TypeA2)
        type_a3 = TypeA(value=type_a_3)
        assert isinstance(type_a3, TypeA)
        assert isinstance(type_a3.value, TypeA3)

    def test_type_a_to_primitives(self):
        type_a_1 = TypeA1(a1=1)
        type_a_2 = TypeA2(a1=1.0, a2=True)
        type_a_3 = TypeA3(a1=1.0, a2=True, a3=1)
        type_a1 = TypeA(value=type_a_1)
        assert type_a1.to_primitives() == {
            "value": {"__type": "TypeA1", "a1": 1}}
        type_a2 = TypeA(value=type_a_2)
        assert type_a2.to_primitives() == {
            "value": {"__type": "TypeA2", "a1": 1.0, "a2": True}}
        type_a3 = TypeA(value=type_a_3)
        assert type_a3.to_primitives() == {
            "value": {"__type": "TypeA3", "a1": 1.0, "a2": True, "a3": 1}}

    def test_type_a1_from_primitives(self):
        typ_a_1 = {"value": {"a1": 1}}
        type_a1 = TypeA.from_primitives(typ_a_1)
        assert isinstance(type_a1, TypeA)
        assert isinstance(type_a1.value, TypeA1)

    def test_type_a2_from_primitives(self):
        typ_a_2 = {"value": {"a1": 1.0, "a2": True}}
        type_a2 = TypeA.from_primitives(typ_a_2)
        assert isinstance(type_a2, TypeA)
        assert isinstance(type_a2.value, TypeA2)

    def test_type_a3_from_primitives(self):
        typ_a_3 = {"value": {"a1": 1.0, "a2": True, "a3": 1}}
        type_a3 = TypeA.from_primitives(typ_a_3)
        assert isinstance(type_a3, TypeA)
        assert isinstance(type_a3.value, TypeA3)


class TestUnionTypesCastingCattrB(unittest.TestCase):
    def test_type_b(self):
        type_b_1 = TypeB1(b1=1.0, b2=True)
        type_b_2 = TypeB2(b1=1.0, b2=1)
        type_b_3 = TypeB3(b1=1.0, b2=True, b3=1)
        type_b1 = TypeB(value=type_b_1)
        assert isinstance(type_b1, TypeB)
        assert isinstance(type_b1.value, TypeB1)
        type_b2 = TypeB(value=type_b_2)
        assert isinstance(type_b2, TypeB)
        assert isinstance(type_b2.value, TypeB2)
        type_b3 = TypeB(value=type_b_3)
        assert isinstance(type_b3, TypeB)
        assert isinstance(type_b3.value, TypeB3)

    def test_type_b1_from_primitives(self):
        typ_b_1 = {"value": {"__type": "TypeB1", "b1": 1.0, "b2": True}}
        type_b1 = TypeB.from_primitives(typ_b_1)
        assert isinstance(type_b1, TypeB)
        assert isinstance(type_b1.value, TypeB1)

    def test_type_b2_from_primitives(self):
        typ_b_2 = {"value": {"__type": "TypeB2", "b1": 1.0, "b2": 1}}
        type_b2 = TypeB.from_primitives(typ_b_2)
        assert isinstance(type_b2, TypeB)
        assert isinstance(type_b2.value, TypeB2)

    def test_type_b2_from_primitives2(self):
        typ_b_2 = {"value": {"__type": "TypeB2", "b1": 1.0, "b2": 9}}
        type_b2 = TypeB.from_primitives(typ_b_2)
        assert isinstance(type_b2, TypeB)
        assert isinstance(type_b2.value, TypeB2)

    def test_type_b3_from_primitives(self):
        typ_b_3 = {"value": {
            "__type": "TypeB3",
            "b1": 1.0, "b2": True, "b3": 1}}
        type_b3 = TypeB.from_primitives(typ_b_3)
        assert isinstance(type_b3, TypeB)
        assert isinstance(type_b3.value, TypeB3)
