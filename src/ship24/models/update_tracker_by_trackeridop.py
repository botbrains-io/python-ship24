"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .tracker import Tracker, TrackerTypedDict
from datetime import datetime
from enum import Enum
import pydantic
from ship24.types import BaseModel
from ship24.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
from typing import Any, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class UpdateTrackerByTrackerIDSearchBy(str, Enum):
    r"""Parameter allowing to search either by `trackerId`or `clientTrackerId`. Default behavior is by `trackerId`."""

    TRACKER_ID = "trackerId"
    CLIENT_TRACKER_ID = "clientTrackerId"


UpdateTrackerByTrackerIDCourierCodeTypedDict = TypeAliasType(
    "UpdateTrackerByTrackerIDCourierCodeTypedDict", Union[List[Any], str]
)


UpdateTrackerByTrackerIDCourierCode = TypeAliasType(
    "UpdateTrackerByTrackerIDCourierCode", Union[List[Any], str]
)


class UpdateTrackerByTrackerIDRequestBodyTypedDict(TypedDict):
    r"""Only the following property can be updated on a Tracker:"""

    is_subscribed: NotRequired[bool]
    r"""Setting at `false` will unsubscribe you from the `Tracker`. Once unsubscribed, you will still be able to fetch the existing tracking results but Ship24 won't search for new data or send webhook notifications. `Trackers` are automatically disabled after the parcel delivery or after a long period without any new events. Manually unsubscribing your tracker is not useful, except if you wish to stop receiving webhooks on it or if you need to reuse the `clientTrackerId` value in a new `Tracker`."""
    courier_code: NotRequired[UpdateTrackerByTrackerIDCourierCodeTypedDict]
    r"""Code of the courier(s) handling the shipment (Up to 3 max) (see Couriers list section)  - 📌 Recommended to improve tracking accuracy"""
    origin_country_code: NotRequired[str]
    r"""Sender country code."""
    destination_country_code: NotRequired[str]
    r"""Recipient country code - 📌 Recommended to improve tracking accuracy"""
    destination_post_code: NotRequired[str]
    r"""Recipient Post code (or ZIP code)  - 📌 Recommended to improve tracking accuracy"""
    shipping_date: NotRequired[datetime]
    r"""Date at which the shipment has been shipped  - 📌 Recommended to improve tracking accuracy: providing the shipping date helps us accurately identify the shipment and improves our ability to retrieve the correct data. However, an inaccurate shipping date could cause our system to exclude the right shipment. Therefore, please ensure the provided shipping date aligns closely with the actual shipment date, give or take a few days. [Format](http://docs.ship24.com/data-format#logistics-date-and-time)"""


class UpdateTrackerByTrackerIDRequestBody(BaseModel):
    r"""Only the following property can be updated on a Tracker:"""

    is_subscribed: Annotated[Optional[bool], pydantic.Field(alias="isSubscribed")] = (
        None
    )
    r"""Setting at `false` will unsubscribe you from the `Tracker`. Once unsubscribed, you will still be able to fetch the existing tracking results but Ship24 won't search for new data or send webhook notifications. `Trackers` are automatically disabled after the parcel delivery or after a long period without any new events. Manually unsubscribing your tracker is not useful, except if you wish to stop receiving webhooks on it or if you need to reuse the `clientTrackerId` value in a new `Tracker`."""

    courier_code: Annotated[
        Optional[UpdateTrackerByTrackerIDCourierCode],
        pydantic.Field(alias="courierCode"),
    ] = None
    r"""Code of the courier(s) handling the shipment (Up to 3 max) (see Couriers list section)  - 📌 Recommended to improve tracking accuracy"""

    origin_country_code: Annotated[
        Optional[str], pydantic.Field(alias="originCountryCode")
    ] = None
    r"""Sender country code."""

    destination_country_code: Annotated[
        Optional[str], pydantic.Field(alias="destinationCountryCode")
    ] = None
    r"""Recipient country code - 📌 Recommended to improve tracking accuracy"""

    destination_post_code: Annotated[
        Optional[str], pydantic.Field(alias="destinationPostCode")
    ] = None
    r"""Recipient Post code (or ZIP code)  - 📌 Recommended to improve tracking accuracy"""

    shipping_date: Annotated[
        Optional[datetime], pydantic.Field(alias="shippingDate")
    ] = None
    r"""Date at which the shipment has been shipped  - 📌 Recommended to improve tracking accuracy: providing the shipping date helps us accurately identify the shipment and improves our ability to retrieve the correct data. However, an inaccurate shipping date could cause our system to exclude the right shipment. Therefore, please ensure the provided shipping date aligns closely with the actual shipment date, give or take a few days. [Format](http://docs.ship24.com/data-format#logistics-date-and-time)"""


class UpdateTrackerByTrackerIDRequestTypedDict(TypedDict):
    tracker_id: str
    r"""**Required** Id of the tracker, provided by Ship24 at creation. `clientTrackerId` can also be used in this field by employing the `searchBy` parameter."""
    search_by: NotRequired[UpdateTrackerByTrackerIDSearchBy]
    r"""Parameter allowing to search either by `trackerId`or `clientTrackerId`. Default behavior is by `trackerId`."""
    request_body: NotRequired[UpdateTrackerByTrackerIDRequestBodyTypedDict]
    r"""Only the following property can be updated on a Tracker:"""


class UpdateTrackerByTrackerIDRequest(BaseModel):
    tracker_id: Annotated[
        str,
        pydantic.Field(alias="trackerId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""**Required** Id of the tracker, provided by Ship24 at creation. `clientTrackerId` can also be used in this field by employing the `searchBy` parameter."""

    search_by: Annotated[
        Optional[UpdateTrackerByTrackerIDSearchBy],
        pydantic.Field(alias="searchBy"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Parameter allowing to search either by `trackerId`or `clientTrackerId`. Default behavior is by `trackerId`."""

    request_body: Annotated[
        Optional[UpdateTrackerByTrackerIDRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""Only the following property can be updated on a Tracker:"""


class UpdateTrackerByTrackerIDResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: TrackerTypedDict


class UpdateTrackerByTrackerIDResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: Tracker
