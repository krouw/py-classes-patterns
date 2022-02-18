from __future__ import annotations
from abc import ABC

import attrs

"""
attrs raise error when VO has invalid default value
Error discovering unittest tests:
Failed to import test module: inheritance.attrs
Traceback (most recent call last):
File "C:/Users/pipe/AppData/Local/Programs/Python/Python39/lib/unittest/loader.py", line 470, in _find_test_path
package = self._get_module_from_name(name)
File "C:/Users/pipe/AppData/Local/Programs/Python/Python39/lib/unittest/loader.py", line 377, in _get_module_from_name
__import__(name)
File "c:/Users/pipe/Documents/work/codes/python-classes/classes/inheritance/attrs/__init__.py", line 1, in <module>
from .attrs import *
File "c:/Users/pipe/Documents/work/codes/python-classes/classes/inheritance/attrs/attrs.py", line 25, in <module>
class AttenuationTechSpec(TechSpec):
File "c:/Users/pipe/Documents/work/codes/python-classes/classes/inheritance/attrs/attrs.py", line 27, in AttenuationTechSpec
attenuation_1310nm: Attenuation = Attenuation(value=0)
File "<attrs generated init inheritance.attrs.attrs.Attenuation>", line 5, in __init__
__attr_validator_value(self, __attr_value, self.value)
File "C:/Users/pipe/AppData/Local/pypoetry/Cache/virtualenvs/py-classes-bGa7MF8d-py3.9/lib/site-packages/attr/_make.py", line 3096, in __call__
v(inst, attr, value)
File "C:/Users/pipe/AppData/Local/pypoetry/Cache/virtualenvs/py-classes-bGa7MF8d-py3.9/lib/site-packages/attr/validators.py", line 103, in __call__
raise TypeError(
TypeError: ("'value' must be <class 'float'> (got 0 that is a <class 'int'>).", 
Attribute(name='value', default=NOTHING, validator=_AndValidator(_validators=(<instance_of validator for type <class 'float'>>, <Validator for x > 0>)), 
repr=True, eq=True, eq_key=None, order=True, order_key=None, hash=None, init=True, metadata=mappingproxy({}), type='float', converter=None, kw_only=False, 
inherited=False, on_setattr=None), <class 'float'>, 0)
"""


@attrs.define(frozen=True)
class NumberOfFilaments:
    value: int = attrs.field(
        validator=[
            attrs.validators.instance_of(int),
            attrs.validators.gt(0)
        ]
    )


@ attrs.define(frozen=True)
class Attenuation:
    value: float = attrs.field(
        validator=[attrs.validators.instance_of(float), attrs.validators.gt(0)])


class TechSpec(ABC):
    pass


# attrs defaults must define to final
@ attrs.define(frozen=True)
class AttenuationTechSpec(TechSpec):
    attenuation_1550nm: Attenuation = attrs.field(
        validator=[attrs.validators.instance_of(Attenuation)])
    attenuation_1310nm: Attenuation = attrs.field(
        validator=[attrs.validators.instance_of(Attenuation)],
        default=Attenuation(value=1.0))

    @ classmethod
    def from_primitives(cls, primitives: dict) -> AttenuationTechSpec:
        return cls(**primitives)

    def to_primitives(self) -> dict:
        return attrs.asdict(self)


@ attrs.define(frozen=True)
class NumberOfFilamentsTechSpec(TechSpec):
    number_of_filaments: NumberOfFilaments = NumberOfFilaments(value=1)


@ attrs.define(frozen=True)
class ConnectorTechSpec(AttenuationTechSpec):
    @classmethod
    def from_primitives(cls, primitives: dict) -> ConnectorTechSpec:
        return cls(
            attenuation_1310nm=Attenuation(
                value=primitives["attenuation_1310nm"]["value"]),
            attenuation_1550nm=Attenuation(
                value=primitives["attenuation_1550nm"]["value"])
        )


"""
multiple inheritance in attrs cannot be possible for slots constraints :c
https://www.attrs.org/en/stable/glossary.html
https://docs.python.org/3/reference/datamodel.html#notes-on-using-slots
"""


@ attrs.define(frozen=True)
class CableTechSpec:
    attenuation_1550nm: Attenuation = attrs.field(
        validator=[attrs.validators.instance_of(Attenuation)])
    attenuation_1310nm: Attenuation = attrs.field(
        validator=[attrs.validators.instance_of(Attenuation)],
        default=Attenuation(value=1.0))
    number_of_filaments: NumberOfFilaments = NumberOfFilaments(value=1)

    @classmethod
    def from_primitives(cls, primitives: dict) -> CableTechSpec:
        return cls(
            number_of_filaments=NumberOfFilaments(
                value=primitives["number_of_filaments"]["value"]),
            attenuation_1310nm=Attenuation(
                value=primitives["attenuation_1310nm"]["value"]),
            attenuation_1550nm=Attenuation(
                value=primitives["attenuation_1550nm"]["value"])
        )

    def to_primitives(self) -> dict:
        return attrs.asdict(self)
