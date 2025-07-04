"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ship24.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ErrorResponseFormatErrorTypedDict(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]


class ErrorResponseFormatError(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None


class ErrorResponseFormatDataTypedDict(TypedDict):
    pass


class ErrorResponseFormatData(BaseModel):
    pass
