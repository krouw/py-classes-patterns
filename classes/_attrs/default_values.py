import attrs

"""
ERROR: Fields without default values cannot appear after fields with default values
@define
class Base:
    a: int
    b: int = 2


@define
class Child(Base):
    c: int

"""


"""
TypeError: multiple bases have instance lay-out conflict

@attrs.define
class DefaultBase:
    a: int
    b: int = attrs.field(
        validator=[
            attrs.validators.instance_of(int),
            attrs.validators.gt(0)],
        default=0)


@attrs.define
class Base:
    c: int


@attrs.define
class Child(DefaultBase, Base):
    pass
"""


@attrs.define
class Base:
    a: int = attrs.field(
        validator=[
            attrs.validators.instance_of(int)
        ]
    )
    b: int = attrs.field(
        validator=[
            attrs.validators.instance_of(int),
            attrs.validators.gt(0)],
        default=0
    )


@attrs.define
class Child(Base):
    """ Can only add default fields """
    c: int = attrs.field(
        validator=[
            attrs.validators.instance_of(int),
            attrs.validators.gt(0)],
        default=0)
