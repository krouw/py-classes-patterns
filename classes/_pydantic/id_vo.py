# pyright: reportGeneralTypeIssues=false

from __future__ import annotations

from pydantic import BaseModel, constr

from nanoid import generate
from nanoid.resources import alphabet, size


class ID(BaseModel):
    """
        value: constr(min_length=1, max_length=36)
        Statements must be separated by newlines or semicolonsPylance
    """
    value: constr(min_length=1, max_length=36)

    class Config:
        frozen = True

    @staticmethod
    def generate(alphabet=alphabet, size=size) -> ID:
        return ID(value=generate(alphabet=alphabet, size=size))

    def to_primitives(self) -> dict[str, str]:
        return self.dict()
