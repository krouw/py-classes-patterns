# pyright: reportGeneralTypeIssues=false

import unittest

from classes._dataclasses import (
    Attenuation,
    NumberOfFilaments,
    ConnectorTechSpec,
    CableTechSpec
)


class TestInheritanceConnectorDataclasses(unittest.TestCase):
    def test_connector_tech_spec_instance(self):
        tech_spec = ConnectorTechSpec(
            attenuation_1310nm=Attenuation(value=0.5),
            attenuation_1550nm=Attenuation(value=0.6)
        )
        self.assertEqual(tech_spec.attenuation_1310nm.value, 0.5)
        self.assertEqual(tech_spec.attenuation_1550nm.value, 0.6)

    def test_connector_tech_spec_inmutable(self):
        tech_spec = ConnectorTechSpec(
            attenuation_1310nm=Attenuation(value=0.5),
            attenuation_1550nm=Attenuation(value=0.6)
        )
        # pydantic raises TypeError when object is inmutable
        with self.assertRaises(AttributeError):
            tech_spec.attenuation_1310nm = Attenuation(value=0.6)

    def test_connector_tech_spec_error_when_attenuation_default_is_invalid(self):
        with self.assertRaises(TypeError):
            ConnectorTechSpec(
                attenuation_1550nm=0.6,
            )

    def test_connector_tech_spec_error_when_attenuation_is_none(self):
        with self.assertRaises(TypeError):
            ConnectorTechSpec(
                attenuation_1310nm=None,
                attenuation_1550nm=0.6,
            )

    def test_connector_tech_spec_error_when_attenuation_is_zero(self):
        with self.assertRaises(TypeError):
            ConnectorTechSpec(
                attenuation_1310nm=Attenuation(value=0),
                attenuation_1550nm=Attenuation(value=0.6),
            )

    def test_connector_tech_spec_from_primitives(self):
        tech_spec = ConnectorTechSpec.from_primitives(
            {
                "attenuation_1310nm": {"value":  0.5},
                "attenuation_1550nm": {"value":  0.6}
            }
        )
        assert isinstance(tech_spec, ConnectorTechSpec)
        self.assertEqual(tech_spec.attenuation_1310nm.value, 0.5)
        self.assertEqual(tech_spec.attenuation_1550nm.value, 0.6)

    def test_connector_tech_spec_to_primitives(self):
        tech_spec = ConnectorTechSpec(
            attenuation_1310nm=Attenuation(value=0.5),
            attenuation_1550nm=Attenuation(value=0.6)
        )
        self.assertEqual(tech_spec.to_primitives(), {
            "attenuation_1310nm": {"value":  0.5},
            "attenuation_1550nm": {"value":  0.6}
        })


class TestInheritanceCableDataclasses(unittest.TestCase):
    def test_cable_tech_spec_instance(self):
        tech_spec = CableTechSpec(
            attenuation_1310nm=Attenuation(value=0.5),
            attenuation_1550nm=Attenuation(value=0.6),
            number_of_filaments=NumberOfFilaments(value=1)
        )
        self.assertEqual(tech_spec.attenuation_1310nm.value, 0.5)
        self.assertEqual(tech_spec.attenuation_1550nm.value, 0.6)
        self.assertEqual(tech_spec.number_of_filaments.value, 1)

    def test_cable_tech_spec_error_when_attenuation_default_is_invalid(self):
        with self.assertRaises(TypeError):
            CableTechSpec(
                attenuation_1310nm=Attenuation(value=0),
                attenuation_1550nm=Attenuation(value=0.6),
            )

    def test_cable_tech_spec_error_when_attenuation_is_none(self):
        with self.assertRaises(TypeError):
            CableTechSpec(
                attenuation_1310nm=None,
                attenuation_1550nm=Attenuation(value=0.6),
                number_of_filaments=NumberOfFilaments(value=1)
            )

    def test_cable_tech_spec_error_when_number_of_filaments_is_zero(self):
        with self.assertRaises(ValueError):
            CableTechSpec(
                attenuation_1310nm=None,
                attenuation_1550nm=Attenuation(value=0.6),
                number_of_filaments=NumberOfFilaments(value=0)
            )

    def test_cable_tech_spec_from_primitives(self):
        tech_spec = CableTechSpec.from_primitives(
            {
                "attenuation_1310nm": {"value":  0.5},
                "attenuation_1550nm": {"value":  0.6},
                "number_of_filaments": {"value":  1}
            }
        )
        assert isinstance(tech_spec, CableTechSpec)
        self.assertEqual(tech_spec.attenuation_1310nm.value, 0.5)
        self.assertEqual(tech_spec.attenuation_1550nm.value, 0.6)
        self.assertEqual(tech_spec.number_of_filaments.value, 1)

    def test_cable_tech_spec_to_primitives(self):
        tech_spec = CableTechSpec(
            attenuation_1310nm=Attenuation(value=0.5),
            attenuation_1550nm=Attenuation(value=0.6),
            number_of_filaments=NumberOfFilaments(value=1)
        )
        self.assertEqual(tech_spec.to_primitives(), {
            "attenuation_1310nm": {"value":  0.5},
            "attenuation_1550nm": {"value":  0.6},
            "number_of_filaments": {"value":  1}
        })
