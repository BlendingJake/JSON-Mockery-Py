from random import random


class Nothing:
    def __init__(self):
        pass

    def __repr__(self):
        return "NOTHING"

    def __str__(self):
        return "NOTHING"


class Generator:
    Nothing = Nothing()

    def __init__(self, nullable=False, null_probability=0.5):
        self.nullable = nullable
        self.null_probability = null_probability
        self._exhausted = False

    def _one(self):
        raise NotImplementedError()

    def exhausted(self) -> bool:
        return self._exhausted

    def one(self):
        self._exhausted = True
        if self.nullable and random() <= self.null_probability:
            return None
        else:
            return self._one()
