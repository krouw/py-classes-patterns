from typing import Union

import attrs
import cattr

converter = cattr.Converter()


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


converter.register_unstructure_hook(
    Union[TypeA1, TypeA2, TypeA3],
    lambda o: {"__type": type(o).__name__,  **converter.unstructure(o)}
)


@attrs.define
class TypeA:
    value: Union[TypeA1, TypeA2, TypeA3]

    @classmethod
    def from_primitives(cls, value: dict):
        return cattr.structure(value, cls)

    def to_primitives(self):
        return {
            "value": converter.unstructure(self.value, unstructure_as=Union[TypeA1, TypeA2, TypeA3])
        }


@attrs.define
class TypeB1:
    b1: float
    b2: bool


@attrs.define
class TypeB2:
    b1: float
    b2: int


@attrs.define
class TypeB3:
    b1: float
    b2: bool
    b3: int


converter.register_structure_hook(
    Union[TypeB1, TypeB2, TypeB3],
    lambda o, _: converter.structure(
        o, TypeB1 if o["__type"] == "TypeB1" else (
            TypeB2 if o["__type"] == "TypeB2" else TypeB3
        )
    )
)


@attrs.define
class TypeB:
    value: Union[TypeB1, TypeB2, TypeB3]

    """
    not working:
    ValueError: 
    <class 'classes._cattr.union_types.TypeB1'> 
    has no usable unique attributes.

    It's necessary a structured hook
    to convert to the right type

    @classmethod
    def from_primitives(cls, value: dict):
        return cattr.structure(value, cls)

    """

    @classmethod
    def from_primitives(cls, value: dict):
        return converter.structure(value, cls)
