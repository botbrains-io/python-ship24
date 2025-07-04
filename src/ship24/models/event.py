"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import model_serializer
from ship24.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class EventTypedDict(TypedDict):
    event_id: NotRequired[str]
    r"""Unique identifier of the event in Ship24 system."""
    tracking_number: NotRequired[str]
    r"""The original tracking number used to create the Tracker."""
    event_tracking_number: NotRequired[str]
    r"""The tracking number associated with the event, on which the event has been found."""
    status: NotRequired[Nullable[str]]
    r"""Event raw text."""
    occurrence_datetime: NotRequired[str]
    r"""[Date and time](http://docs.ship24.com/data-format#logistics-date-and-time) at which the event occurred."""
    order: NotRequired[Nullable[int]]
    r"""Indicate the order of the events in case the occurrenceDatetime is the same between multiple events (lower is older)."""
    location: NotRequired[Nullable[str]]
    r"""Location raw text of the event."""
    source_code: NotRequired[Nullable[str]]
    r"""Internal code of the source used to get this event. Please note that those codes may evolve at any point in time."""
    courier_code: NotRequired[Nullable[str]]
    r"""Code of the courier linked to this event, refers to our Couriers list. Please note that those codes may evolve at any point in time."""
    status_code: NotRequired[Nullable[str]]
    r"""[statusCode](https://docs.ship24.com/status/#statuscode-and-statuscategory) of the event.

    """
    status_category: NotRequired[Nullable[str]]
    r"""[statusCategory](https://docs.ship24.com/status/#statuscode-and-statuscategory) of the event.

    """
    status_milestone: NotRequired[str]
    r"""[statusMilestone](https://docs.ship24.com/status/#statusmilestone) of the shipment at the time of the event."""
    datetime: NotRequired[str]
    utc_offset: NotRequired[str]
    has_no_time: NotRequired[bool]


class Event(BaseModel):
    event_id: Annotated[Optional[str], pydantic.Field(alias="eventId")] = None
    r"""Unique identifier of the event in Ship24 system."""

    tracking_number: Annotated[
        Optional[str], pydantic.Field(alias="trackingNumber")
    ] = None
    r"""The original tracking number used to create the Tracker."""

    event_tracking_number: Annotated[
        Optional[str], pydantic.Field(alias="eventTrackingNumber")
    ] = None
    r"""The tracking number associated with the event, on which the event has been found."""

    status: OptionalNullable[str] = UNSET
    r"""Event raw text."""

    occurrence_datetime: Annotated[
        Optional[str], pydantic.Field(alias="occurrenceDatetime")
    ] = None
    r"""[Date and time](http://docs.ship24.com/data-format#logistics-date-and-time) at which the event occurred."""

    order: OptionalNullable[int] = UNSET
    r"""Indicate the order of the events in case the occurrenceDatetime is the same between multiple events (lower is older)."""

    location: OptionalNullable[str] = UNSET
    r"""Location raw text of the event."""

    source_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="sourceCode")
    ] = UNSET
    r"""Internal code of the source used to get this event. Please note that those codes may evolve at any point in time."""

    courier_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="courierCode")
    ] = UNSET
    r"""Code of the courier linked to this event, refers to our Couriers list. Please note that those codes may evolve at any point in time."""

    status_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="statusCode")
    ] = UNSET
    r"""[statusCode](https://docs.ship24.com/status/#statuscode-and-statuscategory) of the event.

    """

    status_category: Annotated[
        OptionalNullable[str], pydantic.Field(alias="statusCategory")
    ] = UNSET
    r"""[statusCategory](https://docs.ship24.com/status/#statuscode-and-statuscategory) of the event.

    """

    status_milestone: Annotated[
        Optional[str], pydantic.Field(alias="statusMilestone")
    ] = None
    r"""[statusMilestone](https://docs.ship24.com/status/#statusmilestone) of the shipment at the time of the event."""

    datetime: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None

    utc_offset: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="utcOffset",
        ),
    ] = None

    has_no_time: Annotated[
        Optional[bool],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="hasNoTime",
        ),
    ] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "eventId",
            "trackingNumber",
            "eventTrackingNumber",
            "status",
            "occurrenceDatetime",
            "order",
            "location",
            "sourceCode",
            "courierCode",
            "statusCode",
            "statusCategory",
            "statusMilestone",
            "datetime",
            "utcOffset",
            "hasNoTime",
        ]
        nullable_fields = [
            "status",
            "order",
            "location",
            "sourceCode",
            "courierCode",
            "statusCode",
            "statusCategory",
        ]
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
