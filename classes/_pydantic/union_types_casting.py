from typing import Annotated, Union, Literal

import pydantic


class TypeA1(pydantic.BaseModel):
    a1: int


class TypeA2(pydantic.BaseModel):
    a1: float
    a2: bool


class TypeA3(pydantic.BaseModel):
    a1: float
    a2: bool
    a3: int


class TypeA(pydantic.BaseModel):
    value: Union[TypeA1, TypeA2, TypeA3]

    """
    not working:
    @classmethod
    def from_primitives(cls, primitives: dict):
        return cls(**primitives) """

    """
    not working:
    pydantic cast always to TypeA1
    """
    @classmethod
    def from_primitives(cls, primitives: dict):
        if primitives["value"]["__type"] == "TypeA1":
            return TypeA(value=TypeA1(**primitives["value"]))
        elif primitives["value"]["__type"] == "TypeA2":
            return TypeA(
                value=TypeA2(
                    **primitives["value"]
                )
            )
        elif primitives["value"]["__type"] == "TypeA3":
            return TypeA(
                value=TypeA3(
                    a1=primitives["value"]["a1"],
                    a2=primitives["value"]["a2"],
                    a3=primitives["value"]["a3"]
                )
            )
        else:
            raise ValueError(f"Unknown type {primitives['value']['__type']}")

    def to_primitives(self):
        return {
            "__type": self.value.__class__.__name__,
            **self.value.dict()
        }


class TypeB1(pydantic.BaseModel):
    b1: float
    b2: bool


class TypeB2(pydantic.BaseModel):
    b1: float
    b2: int


class TypeB3(pydantic.BaseModel):
    b1: float
    b2: bool
    b3: int


class TypeB(pydantic.BaseModel):
    value: Union[TypeB1, TypeB2, TypeB3]

    class Config:
        smart_union = True

    @classmethod
    def from_primitives(cls, primitives: dict):
        if primitives["value"]["__type"] == "TypeB1":
            return TypeB(value=TypeB1(**primitives["value"]))
        elif primitives["value"]["__type"] == "TypeB2":
            return TypeB(
                value=TypeB2(
                    **primitives["value"]
                )
            )
        elif primitives["value"]["__type"] == "TypeB3":
            return TypeB(
                value=TypeB3(
                    **primitives["value"]
                )
            )
        else:
            raise ValueError(f"Unknown type {primitives['value']['__type']}")


"""


Type field cannot be __type
"""


class TypeC1(pydantic.BaseModel):
    type: Literal["TypeC1"] = "TypeC1"
    c1: str


class TypeC2(pydantic.BaseModel):
    type: Literal["TypeC2"] = "TypeC2"
    c1: int
    c2: str


class TypeC3(pydantic.BaseModel):
    type: Literal["TypeC3"] = "TypeC3"
    c1: int
    c2: str
    c3: bool


TypeC = Annotated[
    Union[TypeC1, TypeC2, TypeC3],
    pydantic.Field(discriminator="__type")
]


class TypeCBase(pydantic.BaseModel):
    value: Union[TypeC1, TypeC2, TypeC3]

    @classmethod
    def from_primitives(cls, value: dict):
        return cls(**value)
