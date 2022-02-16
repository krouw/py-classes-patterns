from __future__ import annotations

from nanoid import generate
from nanoid.resources import alphabet, size


class ID:
    __slots__ = ('value',)

    def __init__(
        self,
        value: str
    ) -> None:
        self.__validate(value)
        super(ID, self).__setattr__("value", value)

    @classmethod
    def from_primitive(cls, id: dict[str, str]) -> ID:
        return cls(value=id["value"])

    def to_primitives(self) -> dict[str, str]:
        return {
            "value": self.value
        }

    def __validate(self, value: str):
        self.__validate_value_is_str(value=value)
        self.__validate_value_has_valid_lenght(value=value)

    def __validate_value_is_str(self, value: str):
        if not isinstance(value, str):
            raise TypeError(
                f'ID value must be a string, not {type(value)}')

    def __validate_value_has_valid_lenght(self, value: str):
        if len(value) < 1 or len(value) > 36:
            raise ValueError(
                f'ID value must be between 1 and 36 characters long, not {len(value)}')

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, ID):
            return False
        return self.value == __o.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __setattr__(self, name, value):
        """"""
        msg = "'%s' has no attribute %s" % (self.__class__,
                                            name)
        raise AttributeError(msg)

    def __delattr__(self, __name: str) -> None:
        """"""
        msg = "'%s' has no attribute %s" % (self.__class__,
                                            __name)
        raise AttributeError(msg)

    @staticmethod
    def generate(alphabet=alphabet, size=size) -> ID:
        return ID(value=generate(alphabet=alphabet, size=size))
