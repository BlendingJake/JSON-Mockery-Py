from pathlib import Path
from typing import Union, List, TextIO
import json
from pprint import pprint
from .mocks import Number
from .mocks import Object


class Mocker:
    def __init__(self, schema: Object):
        self.schema = schema

    def mock(self, n: Union[int, Number] = 1) -> List[dict]:
        if isinstance(n, Number):
            count = n.one()
        else:
            count = n

        return [
            self.schema.one() for _ in range(count)
        ]

    def fmock(self, path_or_buffer: Union[str, Path, TextIO], n: Union[int, Number] = 1):
        if isinstance(path_or_buffer, (str, Path)):
            with open(path_or_buffer, "w") as file:
                json.dump(self.mock(n), file)
        else:
            json.dump(self.mock(n), path_or_buffer)

    def pmock(self, n: Union[int, Number] = 1):
        pprint(self.mock(n))
