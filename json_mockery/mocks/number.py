from typing import Union
from random import uniform
from .generator import Generator


class Number(Generator):
    def __init__(self, min_=0, max_=1, integer=False, precision=4, *args, **kwargs):
        """
        Create a Number generator
        :param min_: The min value to be generated
        :param max_: The max value to be generated
        :param integer: Whether to return an integer or float
        :param precision: If `integer=False`, the value will be rounded to this
        many decimal places
        """
        super().__init__(*args, **kwargs)
        self.min_ = min_
        self.max_ = max_
        self.integer = integer
        self.precision = precision

    def _one(self) -> Union[int, float]:
        val = uniform(self.min_, self.max_)
        if self.integer:
            return int(val)
        else:
            return round(val, self.precision)
