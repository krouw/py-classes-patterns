from __future__ import annotations
from abc import ABC
from typing import NewType

import pydantic


NumberOfFilaments = NewType("NumberOfFilaments", pydantic.conint(gt=0))
Attenuation = NewType("Attenuation", pydantic.confloat(gt=0))


class TechSpec(pydantic.BaseModel, ABC):
    class Config:
        frozen = True


class AttenuationTechSpec(TechSpec):
    attenuation_1310nm: Attenuation
    attenuation_1550nm: Attenuation

    @ classmethod
    def from_primitives(cls, primitives: dict) -> AttenuationTechSpec:
        return cls(**primitives)

    def to_primitives(self) -> dict:
        return self.dict()


class NumberOfFilamentsTechSpec(TechSpec):
    number_of_filaments: NumberOfFilaments


class ConnectorTechSpecType(AttenuationTechSpec):
    """ Connector Tech Spec class """


class CableTechSpecType(AttenuationTechSpec, NumberOfFilamentsTechSpec):
    """  Cables Tech Spec class """
