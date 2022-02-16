from dataclasses import dataclass


@dataclass
class DefaultBase:
    a: int
    b: int = 0

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        if self.b == 0:
            raise ValueError("b cannot be 0")


@dataclass
class Base:
    c: int


@dataclass
class Child(DefaultBase, Base):
    """ Can only add default fields """
    d: int = 2
