from __future__ import annotations
from abc import ABC

import pydantic


"""
# Same resutl than ConstrainedInt and ConstrainedFloat

class NumberOfFilaments(pydantic.conint(gt=0)):
    pass


class Attenuation(pydantic.confloat(gt=0)):
    pass
"""


class NumberOfFilaments(pydantic.ConstrainedInt):
    gt = 0


class Attenuation(pydantic.ConstrainedFloat):
    gt = 0


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


class ConnectorTechSpecInheritance(AttenuationTechSpec):
    """ Connector Tech Spec class """


class CableTechSpecInheritance(AttenuationTechSpec, NumberOfFilamentsTechSpec):
    """  Cables Tech Spec class """
