from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Distance:
    value: float


@dataclass(frozen=True)
class Label:
    value: str


@dataclass(frozen=True)
class Order:
    value: int


@dataclass(frozen=True)
class Unit:
    label: Label
    distance_to_distribution_board: Distance
    distance_to_main_enclosure_one: Distance
    distance_to_main_enclosure_two: Distance

    def to_primitives(self) -> dict:
        return asdict(self)

    @classmethod
    def from_primitives(cls, primitive: dict) -> Unit:
        return cls(
            label=Label(**primitive['label']),
            distance_to_distribution_board=Distance(
                **primitive['distance_to_distribution_board']),
            distance_to_main_enclosure_one=Distance(
                **primitive['distance_to_main_enclosure_one']),
            distance_to_main_enclosure_two=Distance(
                **primitive['distance_to_main_enclosure_two'])
        )


@dataclass(frozen=True)
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

    @classmethod
    def from_primitives(cls, primitive: dict) -> Level:
        return cls(
            label=Label(**primitive['label']),
            order=Order(**primitive['order']),
            distance_to_lower_link=Distance(
                **primitive['distance_to_lower_link']),
            distance_to_upper_link=Distance(
                **primitive['distance_to_upper_link']),
            units=frozenset([
                Unit.from_primitives(unit)
                for unit in primitive['units']
            ])
        )


@dataclass(frozen=True)
class Building:
    label: Label
    levels: frozenset[Level]

    def to_primitives(self) -> dict:
        return {
            'label': {"value": self.label.value},
            'levels': [level.to_primitives() for level in self.levels]
        }

    @classmethod
    def from_primitives(cls, primitive: dict) -> Building:
        return cls(
            label=Label(**primitive['label']),
            levels=frozenset([
                Level.from_primitives(level)
                for level in primitive['levels']
            ])
        )
