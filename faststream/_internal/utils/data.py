from typing import TypeVar

from faststream._internal.basic_types import AnyDict

TypedDictCls = TypeVar("TypedDictCls")


def filter_by_dict(typed_dict: type[TypedDictCls], data: AnyDict) -> TypedDictCls:
    annotations = typed_dict.__annotations__
    return typed_dict(  # type: ignore[call-arg]
        {k: v for k, v in data.items() if k in annotations},
    )
