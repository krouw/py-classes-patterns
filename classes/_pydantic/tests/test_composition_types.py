import unittest

from classes._pydantic import (
    LabelType,
    DistanceType,
    OrderType,
    UnitType,
    LevelType,
    BuildingTypes,
)


class TestCompositionDataclasses(unittest.TestCase):
    def test_building_instance(self):
        unit_1 = UnitType(
            label=LabelType('unit_label_1'),
            distance_to_distribution_board=DistanceType(1.0),
            distance_to_main_enclosure_one=DistanceType(1.0),
            distance_to_main_enclosure_two=DistanceType(1.0)
        )
        unit_2 = UnitType(
            label=LabelType('unit_label_2'),
            distance_to_distribution_board=DistanceType(1.0),
            distance_to_main_enclosure_one=DistanceType(1.0),
            distance_to_main_enclosure_two=DistanceType(1.0)
        )
        level_1 = LevelType(
            label=LabelType("conserjeria"),
            order=OrderType(1),
            distance_to_lower_link=DistanceType(1.0),
            distance_to_upper_link=DistanceType(1.0),
            units=frozenset([unit_1])
        )
        level_2 = LevelType(
            label=LabelType("level_2"),
            order=OrderType(2),
            distance_to_lower_link=DistanceType(1.0),
            distance_to_upper_link=DistanceType(1.0),
            units=frozenset([unit_2])
        )
        building = BuildingTypes(
            label=LabelType("A"),
            levels=frozenset(
                [
                    level_1,
                    level_2
                ]
            )
        )
        assert isinstance(building, BuildingTypes)

    def test_building_to_primitives(self):
        unit_1 = UnitType(
            label=LabelType('unit_label_1'),
            distance_to_distribution_board=DistanceType(1.0),
            distance_to_main_enclosure_one=DistanceType(1.0),
            distance_to_main_enclosure_two=DistanceType(1.0)
        )
        unit_2 = UnitType(
            label=LabelType('unit_label_2'),
            distance_to_distribution_board=DistanceType(1.0),
            distance_to_main_enclosure_one=DistanceType(1.0),
            distance_to_main_enclosure_two=DistanceType(1.0)
        )
        level_1 = LevelType(
            label=LabelType("conserjeria"),
            order=OrderType(1),
            distance_to_lower_link=DistanceType(1.0),
            distance_to_upper_link=DistanceType(1.0),
            units=frozenset([unit_1])
        )
        level_2 = LevelType(
            label=LabelType("level_2"),
            order=OrderType(2),
            distance_to_lower_link=DistanceType(1.0),
            distance_to_upper_link=DistanceType(1.0),
            units=frozenset([unit_2])
        )
        building = BuildingTypes(
            label=LabelType("A"),
            levels=frozenset([level_1, level_2])
        )
        bulding_dict = building.to_primitives()
        assert bulding_dict == {
            'label': 'A',
            'levels': [
                {
                    'label': 'conserjeria',
                    'order': 1,
                    'distance_to_lower_link': 1.0,
                    'distance_to_upper_link': 1.0,
                    'units': [
                        {
                            'label': 'unit_label_1',
                            'distance_to_distribution_board': 1.0,
                            'distance_to_main_enclosure_one': 1.0,
                            'distance_to_main_enclosure_two': 1.0
                        }
                    ]
                },
                {
                    'label': 'level_2',
                    'order': 2,
                    'distance_to_lower_link': 1.0,
                    'distance_to_upper_link': 1.0,
                    'units': [
                        {
                            'label': 'unit_label_2',
                            'distance_to_distribution_board': 1.0,
                            'distance_to_main_enclosure_one':  1.0,
                            'distance_to_main_enclosure_two':  1.0
                        }
                    ]
                }
            ]
        }

    def test_building_from_primitives(self):
        building_primitives = {
            'label': 'A',
            'levels': [
                {
                    'label': 'conserjeria',
                    'order': 1,
                    'distance_to_lower_link': 1.0,
                    'distance_to_upper_link': 1.0,
                    'units': [
                        {
                            'label': 'unit_label_1',
                            'distance_to_distribution_board': 1.0,
                            'distance_to_main_enclosure_one': 1.0,
                            'distance_to_main_enclosure_two': 1.0
                        }
                    ]
                },
                {
                    'label': 'level_2',
                    'order': 2,
                    'distance_to_lower_link': 1.0,
                    'distance_to_upper_link': 1.0,
                    'units': [
                        {
                            'label': 'unit_label_2',
                            'distance_to_distribution_board': 1.0,
                            'distance_to_main_enclosure_one':  1.0,
                            'distance_to_main_enclosure_two':  1.0
                        }
                    ]
                }
            ]
        }
        building = BuildingTypes.from_primitives(building_primitives)
        assert isinstance(building, BuildingTypes)
