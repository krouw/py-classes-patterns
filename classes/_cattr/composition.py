from __future__ import annotations

import attrs
import cattr


@attrs.define(frozen=True)
class Distance:
    value: float


@attrs.define(frozen=True)
class Label:
    value: str


@attrs.define(frozen=True)
class Order:
    value: int


@attrs.define(frozen=True)
class Unit:
    label: Label
    distance_to_distribution_board: Distance
    distance_to_main_enclosure_one: Distance
    distance_to_main_enclosure_two: Distance

    def to_primitives(self) -> dict:
        return cattr.unstructure(self)


@attrs.define(frozen=True)
class Level:
    label: Label
    order: Order
    distance_to_lower_link: Distance
    distance_to_upper_link: Distance
    units: frozenset[Unit]

    def to_primitives(self) -> dict:
        return {
            'label': {"value": self.label.value},
            'order': {"value": self.order.value},
            'distance_to_lower_link': {"value": self.distance_to_lower_link.value},
            'distance_to_upper_link': {"value": self.distance_to_upper_link.value},
            'units': [unit.to_primitives() for unit in self.units]
        }


@attrs.define(frozen=True)
class Building:
    label: Label
    levels: frozenset[Level]

    def to_primitives(self):
        return {
            'label': {"value": self.label.value},
            'levels': [level.to_primitives() for level in self.levels]
        }

    @classmethod
    def from_primitives(cls, primitive: dict) -> Building:
        return cattr.structure(primitive, cls)
