import unittest

from classes._pydantic import (
    DistanceStrictType,
    LabelStrictType,
    OrderStrictType,
    UnitStrictType,
    LevelStrictType,
    BuildingStrictType,
)


class TestCompositionDataclasses(unittest.TestCase):
    def test_building_instance(self):
        unit_1 = UnitStrictType(
            label=LabelStrictType('unit_label_1'),
            distance_to_distribution_board=DistanceStrictType(1.0),
            distance_to_main_enclosure_one=DistanceStrictType(1.0),
            distance_to_main_enclosure_two=DistanceStrictType(1.0)
        )
        unit_2 = UnitStrictType(
            label=LabelStrictType('unit_label_2'),
            distance_to_distribution_board=DistanceStrictType(1.0),
            distance_to_main_enclosure_one=DistanceStrictType(1.0),
            distance_to_main_enclosure_two=DistanceStrictType(1.0)
        )
        level_1 = LevelStrictType(
            label=LabelStrictType("conserjeria"),
            order=OrderStrictType(1),
            distance_to_lower_link=DistanceStrictType(1.0),
            distance_to_upper_link=DistanceStrictType(1.0),
            units=frozenset([unit_1])
        )
        level_2 = LevelStrictType(
            label=LabelStrictType("level_2"),
            order=OrderStrictType(2),
            distance_to_lower_link=DistanceStrictType(1.0),
            distance_to_upper_link=DistanceStrictType(1.0),
            units=frozenset([unit_2])
        )
        building = BuildingStrictType(
            label=LabelStrictType("A"),
            levels=frozenset(
                [
                    level_1,
                    level_2
                ]
            )
        )
        assert isinstance(building, BuildingStrictType)

    def test_building_to_primitives(self):
        unit_1 = UnitStrictType(
            label=LabelStrictType('unit_label_1'),
            distance_to_distribution_board=DistanceStrictType(1.0),
            distance_to_main_enclosure_one=DistanceStrictType(1.0),
            distance_to_main_enclosure_two=DistanceStrictType(1.0)
        )
        unit_2 = UnitStrictType(
            label=LabelStrictType('unit_label_2'),
            distance_to_distribution_board=DistanceStrictType(1.0),
            distance_to_main_enclosure_one=DistanceStrictType(1.0),
            distance_to_main_enclosure_two=DistanceStrictType(1.0)
        )
        level_1 = LevelStrictType(
            label=LabelStrictType("conserjeria"),
            order=OrderStrictType(1),
            distance_to_lower_link=DistanceStrictType(1.0),
            distance_to_upper_link=DistanceStrictType(1.0),
            units=frozenset([unit_1])
        )
        level_2 = LevelStrictType(
            label=LabelStrictType("level_2"),
            order=OrderStrictType(2),
            distance_to_lower_link=DistanceStrictType(1.0),
            distance_to_upper_link=DistanceStrictType(1.0),
            units=frozenset([unit_2])
        )
        building = BuildingStrictType(
            label=LabelStrictType("A"),
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
        building = BuildingStrictType.from_primitives(building_primitives)
        assert isinstance(building, BuildingStrictType)
