from typing import NewType

import pydantic

DistanceType = NewType("Distance", pydantic.confloat(ge=0))
LabelType = NewType(
    "Label",
    pydantic.constr(
        min_length=1,
        max_length=16
    )
)
OrderType = NewType("Order", pydantic.conint(gt=0))


class UnitType(pydantic.BaseModel):
    label: LabelType
    distance_to_distribution_board: DistanceType
    distance_to_main_enclosure_one: DistanceType
    distance_to_main_enclosure_two: DistanceType

    class Config:
        frozen = True


class LevelType(pydantic.BaseModel):
    label: LabelType
    order: OrderType
    distance_to_lower_link: DistanceType
    distance_to_upper_link: DistanceType
    units: frozenset[UnitType]

    class Config:
        frozen = True

    def to_primitives(self):
        return {
            'label': self.label,
            'order': self.order,
            'distance_to_lower_link': self.distance_to_lower_link,
            'distance_to_upper_link': self.distance_to_upper_link,
            'units': [unit.dict() for unit in self.units]
        }


class BuildingTypes(pydantic.BaseModel):
    label: LabelType
    levels: frozenset[LevelType]

    class Config:
        frozen = True

    @classmethod
    def from_primitives(cls, primitives):
        return cls(
            **primitives,
        )

    def to_primitives(self):
        """
        unhashable type: dict when use frozenset
        self.dict()
        """
        b_dict = dict(self)
        l_list = []
        for level in self.levels:
            l_list.append(level.to_primitives())
        return {
            **b_dict,
            "levels": l_list,
        }
