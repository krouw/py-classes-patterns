from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class NumberOfFilaments:
    value: int

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        self.__validate_value_is_int()
        self.__validate_value_is_greater_than_0()

    def __validate_value_is_int(self):
        if not isinstance(self.value, int):
            raise TypeError(
                f"NumberOfFilaments value must be an int, not {self.value}")

    def __validate_value_is_greater_than_0(self):
        if self.value <= 0:
            raise ValueError(
                f'Number of filaments must be greater than 0, not {self.value}')


@dataclass(frozen=True)
class Attenuation:
    value: float

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        self.__validate_value_is_float()
        self.__validate_value_is_greater_than_0()

    def __validate_value_is_float(self):
        if not isinstance(self.value, float):
            raise TypeError(
                f"Attenuation value must be a float, not {self.value}")

    def __validate_value_is_greater_than_0(self):
        if self.value <= 0:
            raise ValueError(
                f'Attenuation value must be greater than 0, not {self.value}')


class TechSpec:
    pass


@dataclass(frozen=True)
class AttenuationTechSpec(TechSpec):
    attenuation_1310nm: Attenuation
    attenuation_1550nm: Attenuation

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        self.__validate_has_valid_attenuations()

    def __validate_has_valid_attenuations(self):
        if not isinstance(self.attenuation_1310nm, Attenuation):
            raise TypeError(
                f"FoEquipmentAttenuationTechSpec.attenuation_1310nm must be an Attenuation, not {self.attenuation_1310nm}")
        if not isinstance(self.attenuation_1550nm, Attenuation):
            raise TypeError(
                f"FoEquipmentAttenuationTechSpec.attenuation_1550nm must be an Attenuation, not {self.attenuation_1550nm}")

    @classmethod
    def from_primitives(cls, primitives: dict) -> AttenuationTechSpec:
        return cls(
            attenuation_1310nm=Attenuation(
                value=primitives["attenuation_1310nm"]["value"]),
            attenuation_1550nm=Attenuation(
                value=primitives["attenuation_1550nm"]["value"])
        )

    def to_primitives(self) -> dict:
        return {
            "attenuation_1310nm": {
                "value": self.attenuation_1310nm.value
            },
            "attenuation_1550nm": {
                "value": self.attenuation_1550nm.value
            }
        }


@dataclass(frozen=True)
class NumberOfFilamentsTechSpec(TechSpec):
    number_of_filaments: NumberOfFilaments

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        self.__validate_has_valid_number_of_filaments()

    def __validate_has_valid_number_of_filaments(self):
        if not isinstance(self.number_of_filaments, NumberOfFilaments):
            raise TypeError(
                f"FoEquipmentNumberOfFilamentsTechSpec.number_of_filaments must be a NumberOfFilaments, not {self.number_of_filaments}")

    @classmethod
    def from_primitives(cls, primitives: dict) -> NumberOfFilamentsTechSpec:
        return cls(
            number_of_filaments=NumberOfFilaments(
                value=primitives["number_of_filaments"])
        )

    def to_primitives(self) -> dict:
        return {
            "number_of_filaments": {"value": self.number_of_filaments.value}
        }


@dataclass(frozen=True)
class ConnectorTechSpec(AttenuationTechSpec):
    @classmethod
    def from_primitives(cls, primitives: dict) -> ConnectorTechSpec:
        return cls(
            attenuation_1310nm=Attenuation(
                value=primitives["attenuation_1310nm"]["value"]),
            attenuation_1550nm=Attenuation(
                value=primitives["attenuation_1550nm"]["value"])
        )


@dataclass(frozen=True)
class CableTechSpec(AttenuationTechSpec, NumberOfFilamentsTechSpec):
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
        return {
            "number_of_filaments": {"value": self.number_of_filaments.value},
            "attenuation_1310nm": {"value": self.attenuation_1310nm.value},
            "attenuation_1550nm": {"value": self.attenuation_1550nm.value}
        }
