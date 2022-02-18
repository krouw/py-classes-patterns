# pyright: reportGeneralTypeIssues=false


from __future__ import annotations

import attrs
from attrs import define, asdict, field


from nanoid import generate
from nanoid.resources import alphabet, size

# https://stackoverflow.com/questions/51972203/custom-validator-in-python-attrs-with-extra-parameters


def make_range_validator(min_value, max_value):
    def range_validator(instance, attribute, value):
        lv = len(value)
        if min_value > lv or lv > max_value:
            raise ValueError(
                "Must be between {} and {}".format(min_value, max_value))

    return range_validator


@define(frozen=True)
class ID:
    value: str = field(
        validator=[attrs.validators.instance_of(str), make_range_validator(1, 36)])

    @staticmethod
    def generate(alphabet=alphabet, size=size) -> ID:
        return ID(value=generate(alphabet=alphabet, size=size))

    def to_primitives(self) -> dict[str, str]:
        return asdict(self)
