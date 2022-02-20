import pydantic


class DistanceStrictType(pydantic.ConstrainedFloat):
    ge = 0


class LabelStrictType(pydantic.ConstrainedStr):
    min_length = 1
    max_length = 16


class OrderStrictType(pydantic.ConstrainedInt):
    gt = 0


class UnitStrictType(pydantic.BaseModel):
    label: LabelStrictType
    distance_to_distribution_board: DistanceStrictType
    distance_to_main_enclosure_one: DistanceStrictType
    distance_to_main_enclosure_two: DistanceStrictType

    class Config:
        frozen = True


class LevelStrictType(pydantic.BaseModel):
    label: LabelStrictType
    order: OrderStrictType
    distance_to_lower_link: DistanceStrictType
    distance_to_upper_link: DistanceStrictType
    units: frozenset[UnitStrictType]

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


class BuildingStrictType(pydantic.BaseModel):
    label: LabelStrictType
    levels: frozenset[LevelStrictType]

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
