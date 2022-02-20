import unittest

from classes._cattr import (
    Building,
    Label,
    Distance,
    Order,
    Level,
    Unit
)


class TestCompositionAttrs(unittest.TestCase):
    def test_building_instance(self):
        unit_1 = Unit(
            label=Label(value='unit_label_1'),
            distance_to_distribution_board=Distance(value=1.0),
            distance_to_main_enclosure_one=Distance(value=1.0),
            distance_to_main_enclosure_two=Distance(value=1.0)
        )
        unit_2 = Unit(
            label=Label(value='unit_label_2'),
            distance_to_distribution_board=Distance(value=1.0),
            distance_to_main_enclosure_one=Distance(value=1.0),
            distance_to_main_enclosure_two=Distance(value=1.0)
        )
        level_1 = Level(
            label=Label(value="conserjeria"),
            order=Order(value=1),
            distance_to_lower_link=Distance(value=1.0),
            distance_to_upper_link=Distance(value=1.0),
            units=frozenset([unit_1])
        )
        level_2 = Level(
            label=Label(value="level_2"),
            order=Order(value=2),
            distance_to_lower_link=Distance(value=1.0),
            distance_to_upper_link=Distance(value=1.0),
            units=frozenset([unit_2])
        )
        building = Building(
            label=Label(value="A"),
            levels=frozenset([level_1, level_2])
        )
        assert isinstance(building, Building)

    def test_building_to_primitives(self):
        unit_1 = Unit(
            label=Label(value='unit_label_1'),
            distance_to_distribution_board=Distance(value=1.0),
            distance_to_main_enclosure_one=Distance(value=1.0),
            distance_to_main_enclosure_two=Distance(value=1.0)
        )
        unit_2 = Unit(
            label=Label(value='unit_label_2'),
            distance_to_distribution_board=Distance(value=1.0),
            distance_to_main_enclosure_one=Distance(value=1.0),
            distance_to_main_enclosure_two=Distance(value=1.0)
        )
        level_1 = Level(
            label=Label(value="conserjeria"),
            order=Order(value=1),
            distance_to_lower_link=Distance(value=1.0),
            distance_to_upper_link=Distance(value=1.0),
            units=frozenset([unit_1])
        )
        level_2 = Level(
            label=Label(value="level_2"),
            order=Order(value=2),
            distance_to_lower_link=Distance(value=1.0),
            distance_to_upper_link=Distance(value=1.0),
            units=frozenset([unit_2])
        )
        building = Building(
            label=Label(value="A"),
            levels=frozenset([level_1, level_2])
        )
        assert building.to_primitives() == {
            'label': {'value': 'A'},
            'levels': [
                {
                    'label': {'value': 'conserjeria'},
                    'order': {'value': 1},
                    'distance_to_lower_link': {'value': 1.0},
                    'distance_to_upper_link': {'value': 1.0},
                    'units': [
                        {
                            'label': {'value': 'unit_label_1'},
                            'distance_to_distribution_board': {'value': 1.0},
                            'distance_to_main_enclosure_one': {'value': 1.0},
                            'distance_to_main_enclosure_two': {'value': 1.0}
                        }
                    ]
                },
                {
                    'label': {'value': 'level_2'},
                    'order': {'value': 2},
                    'distance_to_lower_link': {'value': 1.0},
                    'distance_to_upper_link': {'value': 1.0},
                    'units': [
                        {
                            'label': {'value': 'unit_label_2'},
                            'distance_to_distribution_board': {'value': 1.0},
                            'distance_to_main_enclosure_one': {'value': 1.0},
                            'distance_to_main_enclosure_two': {'value': 1.0}
                        }
                    ]
                }
            ]
        }

    def test_building_from_primitives(self):
        building_primitives = {
            'label': {'value': 'A'},
            'levels': [
                {
                    'label': {'value': 'conserjeria'},
                    'order': {'value': 1},
                    'distance_to_lower_link': {'value': 1.0},
                    'distance_to_upper_link': {'value': 1.0},
                    'units': [
                        {
                            'label': {'value': 'unit_label_1'},
                            'distance_to_distribution_board': {'value': 1.0},
                            'distance_to_main_enclosure_one': {'value': 1.0},
                            'distance_to_main_enclosure_two': {'value': 1.0}
                        }
                    ]
                },
                {
                    'label': {'value': 'level_2'},
                    'order': {'value': 2},
                    'distance_to_lower_link': {'value': 1.0},
                    'distance_to_upper_link': {'value': 1.0},
                    'units': [
                        {
                            'label': {'value': 'unit_label_2'},
                            'distance_to_distribution_board': {'value': 1.0},
                            'distance_to_main_enclosure_one': {'value': 1.0},
                            'distance_to_main_enclosure_two': {'value': 1.0}
                        }
                    ]
                }
            ]
        }
        building = Building.from_primitives(building_primitives)
        assert isinstance(building, Building)
        assert isinstance(building.label, Label)
        assert isinstance(building.levels, frozenset)
        level = list(building.levels)[0]
        assert isinstance(list(building.levels)[0], Level)
        unit = list(level.units)[0]
        assert isinstance(unit, Unit)
