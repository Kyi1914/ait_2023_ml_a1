import datetime
from abc import abstractmethod
from typing import Any, overload

class BaseTzInfo(datetime.tzinfo):
    zone: str | None  # Actually None but should be set on concrete subclasses
    # The following abstract methods don't exist in the implementation, but
    # are implemented by all sub-classes.
    @abstractmethod
    def localize(self, dt: datetime.datetime) -> datetime.datetime: ...
    @abstractmethod
    def normalize(self, dt: datetime.datetime) -> datetime.datetime: ...
    @abstractmethod
    def tzname(self, dt: datetime.datetime | None) -> str: ...
    @abstractmethod
    def utcoffset(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...
    @abstractmethod
    def dst(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...

class StaticTzInfo(BaseTzInfo):
    def fromutc(self, dt: datetime.datetime) -> datetime.datetime: ...
    def localize(self, dt: datetime.datetime, is_dst: bool | None = False) -> datetime.datetime: ...
    def normalize(self, dt: datetime.datetime, is_dst: bool | None = False) -> datetime.datetime: ...
    def tzname(self, dt: datetime.datetime | None, is_dst: bool | None = None) -> str: ...
    def utcoffset(self, dt: datetime.datetime | None, is_dst: bool | None = None) -> datetime.timedelta: ...
    def dst(self, dt: datetime.datetime | None, is_dst: bool | None = None) -> datetime.timedelta: ...

class DstTzInfo(BaseTzInfo):
    def __init__(self, _inf: Any = None, _tzinfos: Any = None) -> None: ...
    def fromutc(self, dt: datetime.datetime) -> datetime.datetime: ...
    def localize(self, dt: datetime.datetime, is_dst: bool | None = False) -> datetime.datetime: ...
    def normalize(self, dt: datetime.datetime) -> datetime.datetime: ...
    def tzname(self, dt: datetime.datetime | None, is_dst: bool | None = None) -> str: ...
    # https://github.com/python/mypy/issues/12379
    @overload  # type: ignore[override]
    def utcoffset(self, dt: None, is_dst: bool | None = None) -> None: ...
    @overload
    def utcoffset(self, dt: datetime.datetime, is_dst: bool | None = None) -> datetime.timedelta: ...
    def dst(self, dt: datetime.datetime | None, is_dst: bool | None = None) -> datetime.timedelta | None: ...
