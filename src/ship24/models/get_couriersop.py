"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from pydantic import model_serializer
from ship24.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RequiredField(str, Enum):
    DESTINATION_POST_CODE = "destinationPostCode"
    DESTINATION_COUNTRY_CODE = "destinationCountryCode"


class CourierTypedDict(TypedDict):
    courier_code: NotRequired[str]
    r"""The codified code of this courier in Ship24 system."""
    courier_name: NotRequired[str]
    r"""The courier name."""
    website: NotRequired[Nullable[str]]
    r"""The courier public website."""
    is_post: NotRequired[bool]
    r"""`true` in case the courier is a postal operator."""
    country_code: NotRequired[Nullable[str]]
    r"""The main country in which the courier is operating."""
    required_fields: NotRequired[Nullable[List[RequiredField]]]
    r"""Indicate which additional information is required by the courier to get optimal tracking results. See [Additional information](https://docs.ship24.com/couriers#required-fields)"""
    is_deprecated: NotRequired[bool]
    r"""`true` in case the courier is deprecated. See [Deprecated couriers](https://docs.ship24.com/couriers#deprecated-couriers)"""


class Courier(BaseModel):
    courier_code: Annotated[Optional[str], pydantic.Field(alias="courierCode")] = None
    r"""The codified code of this courier in Ship24 system."""

    courier_name: Annotated[Optional[str], pydantic.Field(alias="courierName")] = None
    r"""The courier name."""

    website: OptionalNullable[str] = UNSET
    r"""The courier public website."""

    is_post: Annotated[Optional[bool], pydantic.Field(alias="isPost")] = None
    r"""`true` in case the courier is a postal operator."""

    country_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="countryCode")
    ] = UNSET
    r"""The main country in which the courier is operating."""

    required_fields: Annotated[
        OptionalNullable[List[RequiredField]], pydantic.Field(alias="requiredFields")
    ] = UNSET
    r"""Indicate which additional information is required by the courier to get optimal tracking results. See [Additional information](https://docs.ship24.com/couriers#required-fields)"""

    is_deprecated: Annotated[Optional[bool], pydantic.Field(alias="isDeprecated")] = (
        None
    )
    r"""`true` in case the courier is deprecated. See [Deprecated couriers](https://docs.ship24.com/couriers#deprecated-couriers)"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "courierCode",
            "courierName",
            "website",
            "isPost",
            "countryCode",
            "requiredFields",
            "isDeprecated",
        ]
        nullable_fields = ["website", "countryCode", "requiredFields"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetCouriersDataTypedDict(TypedDict):
    couriers: NotRequired[List[CourierTypedDict]]


class GetCouriersData(BaseModel):
    couriers: Optional[List[Courier]] = None


class GetCouriersResponseBodyTypedDict(TypedDict):
    r"""OK"""

    data: NotRequired[GetCouriersDataTypedDict]


class GetCouriersResponseBody(BaseModel):
    r"""OK"""

    data: Optional[GetCouriersData] = None


class GetCouriersResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetCouriersResponseBodyTypedDict


class GetCouriersResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetCouriersResponseBody
