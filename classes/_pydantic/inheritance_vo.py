from __future__ import annotations
from abc import ABC

import pydantic

"""
Pydantic raise error when VO has invalid default value
Error discovering unittest tests:
 Failed to import test module: inheritance.pydantic
Traceback (most recent call last):
  File "C:/Users/pipe/AppData/Local/Programs/Python/Python39/lib/unittest/loader.py", line 470, in _find_test_path
    package = self._get_module_from_name(name)
  File "C:/Users/pipe/AppData/Local/Programs/Python/Python39/lib/unittest/loader.py", line 377, in _get_module_from_name
    __import__(name)
  File "c:/Users/pipe/Documents/work/codes/python-classes/classes/inheritance/pydantic/__init__.py", line 3, in <module>
    from .pydantic_vo import *
  File "c:/Users/pipe/Documents/work/codes/python-classes/classes/inheritance/pydantic/pydantic_vo.py", line 25, in <module>
    class AttenuationTechSpec(TechSpec):
  File "c:/Users/pipe/Documents/work/codes/python-classes/classes/inheritance/pydantic/pydantic_vo.py", line 26, in AttenuationTechSpec
    attenuation_1310nm: AttenuationVO = AttenuationVO(value=0)
  File "pydantic/main.py", line 331, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for AttenuationVO
value
  ensure this value is greater than 0 (type=value_error.number.not_gt; limit_value=0)
"""


class NumberOfFilamentsVO(pydantic.BaseModel):
    value: int = pydantic.Field(gt=0)


class AttenuationVO(pydantic.BaseModel):
    value: float = pydantic.Field(gt=0)


class TechSpec(pydantic.BaseModel, ABC):
    class Config:
        frozen = True


class AttenuationTechSpec(TechSpec):
    attenuation_1310nm: AttenuationVO = AttenuationVO(value=1)
    attenuation_1550nm: AttenuationVO

    @ classmethod
    def from_primitives(cls, primitives: dict) -> AttenuationTechSpec:
        return cls(**primitives)

    def to_primitives(self) -> dict:
        return self.dict()


class NumberOfFilamentsTechSpec(TechSpec):
    number_of_filaments: NumberOfFilamentsVO = NumberOfFilamentsVO(value=1)


class ConnectorTechSpecVO(AttenuationTechSpec):
    """ Connector Tech Spec class """


class CableTechSpecVO(AttenuationTechSpec, NumberOfFilamentsTechSpec):
    """  Cables Tech Spec class """
