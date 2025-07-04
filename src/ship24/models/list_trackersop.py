"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .tracker import Tracker, TrackerTypedDict
from enum import Enum
from ship24.types import BaseModel
from ship24.utils import FieldMetadata, QueryParamMetadata
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class Sort(int, Enum):
    r"""Defines the sorting order of trackers. Use `1` for ascending (`createdAt` oldest first) and `-1` for descending (`createdAt` newest first). The default is ascending (`1`) to ensure stable pagination."""

    ONE = 1
    MINUS_1 = -1


class ListTrackersRequestTypedDict(TypedDict):
    page: int
    r"""The page index, starting from 1."""
    limit: int
    r"""The maximum number of trackers returned per page."""
    sort: NotRequired[Sort]
    r"""Defines the sorting order of trackers. Use `1` for ascending (`createdAt` oldest first) and `-1` for descending (`createdAt` newest first). The default is ascending (`1`) to ensure stable pagination."""


class ListTrackersRequest(BaseModel):
    page: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The page index, starting from 1."""

    limit: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The maximum number of trackers returned per page."""

    sort: Annotated[
        Optional[Sort],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Defines the sorting order of trackers. Use `1` for ascending (`createdAt` oldest first) and `-1` for descending (`createdAt` newest first). The default is ascending (`1`) to ensure stable pagination."""


class ListTrackersXMLResponseBodyTypedDict(TypedDict):
    r"""OK"""

    xml_content: NotRequired[str]


class ListTrackersXMLResponseBody(BaseModel):
    r"""OK"""

    xml_content: Optional[str] = None


class ListTrackersDataTypedDict(TypedDict):
    trackers: NotRequired[List[TrackerTypedDict]]


class ListTrackersData(BaseModel):
    trackers: Optional[List[Tracker]] = None


class ListTrackersResponseBodyTypedDict(TypedDict):
    r"""OK"""

    data: NotRequired[ListTrackersDataTypedDict]


class ListTrackersResponseBody(BaseModel):
    r"""OK"""

    data: Optional[ListTrackersData] = None


ListTrackersResponseResultTypedDict = TypeAliasType(
    "ListTrackersResponseResultTypedDict",
    Union[ListTrackersResponseBodyTypedDict, bytes],
)


ListTrackersResponseResult = TypeAliasType(
    "ListTrackersResponseResult", Union[ListTrackersResponseBody, bytes]
)


class ListTrackersResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ListTrackersResponseResultTypedDict


class ListTrackersResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ListTrackersResponseResult
