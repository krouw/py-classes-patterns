import pydantic


class IntValueInheritance(pydantic.ConstrainedInt):
    gt = 0


class BaseInheritance(pydantic.BaseModel):
    a: int
    b: IntValueInheritance = IntValueInheritance(0)


class ChildInheritance(BaseInheritance):
    c: int
    d: int = 2
