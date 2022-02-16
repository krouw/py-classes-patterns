from dataclasses import dataclass

"""
ERROR: Fields without default values cannot appear after fields with default values
@dataclass
class BaseA:
    a: int
    b: int = 2


@dataclass
class ChildA(BaseA):
    c: int

"""

# SOLUTION


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
