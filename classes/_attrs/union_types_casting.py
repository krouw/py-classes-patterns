from typing import Union

import attrs


@attrs.define
class TypeA1:
    a1: int


@attrs.define
class TypeA2:
    a1: float
    a2: bool


@attrs.define
class TypeA3:
    a1: float
    a2: bool
    a3: int


@attrs.define
class TypeA:
    value: Union[TypeA1, TypeA2, TypeA3]

    @classmethod
    def from_primitives(cls, primitives: dict):
        if primitives["value"]["__type"] == "TypeA1":
            return TypeA(TypeA1(a1=primitives["value"]["a1"]))
        elif primitives["value"]["__type"] == "TypeA2":
            return TypeA(
                TypeA2(
                    a1=primitives["value"]["a1"],
                    a2=primitives["value"]["a2"]
                )
            )
        elif primitives["value"]["__type"] == "TypeA3":
            return TypeA(TypeA3(
                a1=primitives["value"]["a1"],
                a2=primitives["value"]["a2"],
                a3=primitives["value"]["a3"]
            ))
        else:
            raise ValueError(f"Unknown type {primitives['value']['__type']}")

    def to_primitives(self):
        return {
            "value": {
                "__type": self.value.__class__.__name__,
                **attrs.asdict(self.value)
            }
        }
