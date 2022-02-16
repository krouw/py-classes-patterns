from __future__ import annotations

from dataclasses import dataclass
import dataclasses

from nanoid import generate
from nanoid.resources import alphabet, size


@dataclass(frozen=True)
class ID:
    value: str

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        self.__validate_value_is_str()
        self.__validate_value_has_valid_lenght()

    def __validate_value_is_str(self):
        if not isinstance(self.value, str):
            raise TypeError(
                f'ID value must be a string, not {type(self.value)}')

    def __validate_value_has_valid_lenght(self):
        if len(self.value) < 1 or len(self.value) > 36:
            raise ValueError(
                f'ID value must be between 1 and 36 characters long, not {len(self.value)}')

    def to_primitives(self) -> dict[str, str]:
        return dataclasses.asdict(self)

    @staticmethod
    def generate(alphabet=alphabet, size=size) -> ID:
        return ID(value=generate(alphabet=alphabet, size=size))
