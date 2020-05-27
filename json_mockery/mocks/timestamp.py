from datetime import datetime, timezone, timedelta
from typing import Union
from .number import Number

TimestampType = Union[int, float, datetime]


class Timestamp(Number):
    def __init__(
        self,
        earliest: TimestampType = None,
        latest: TimestampType = None,
        milliseconds=False,
        *args, **kwargs
    ):
        """
        Create a timestamp generator
        :param earliest: The datetime of the earliest timestamp to create. Defaults to Now - 365 days.
        :param latest: The datetime of the latest timestamp to create. Defaults to Now.
        :param milliseconds: Whether to return the timestamp in milliseconds or seconds.
        :param args:
        :param kwargs:
        """
        early = Timestamp._to_timestamp(earliest if earliest is not None else datetime.now() - timedelta(days=365))
        late = Timestamp._to_timestamp(latest if latest is not None else datetime.now())

        if milliseconds:
            early *= 1000
            late *= 1000

        super().__init__(
            min_=early,
            max_=late,
            integer=True,
            *args, **kwargs
        )

    @classmethod
    def _to_timestamp(cls, value: TimestampType) -> float:
        if isinstance(value, datetime):
            dt = value
        else:
            dt = datetime.fromtimestamp(value)

        return dt.replace(tzinfo=timezone.utc).timestamp()
