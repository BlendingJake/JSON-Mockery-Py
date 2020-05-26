from uuid import uuid4
from .generator import Generator


class UUID(Generator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _one(self) -> str:
        return str(uuid4()).replace("-", "")
