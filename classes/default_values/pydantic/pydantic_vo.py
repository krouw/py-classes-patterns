import pydantic


class IntValueVO(pydantic.BaseModel):
    value: pydantic.conint(gt=0)  # type: ignore


class BaseVO(pydantic.BaseModel):
    a: int
    """
    b: IntValueVO = IntValueVO(value=0) 
    raise ERROR pydantic.error_wrappers.ValidationError: 1 validation error for IntValueVO
    """
    b: IntValueVO = IntValueVO(value=1)


class ChildVO(BaseVO):
    c: int
    d: int = 2
