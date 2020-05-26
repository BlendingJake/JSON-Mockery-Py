from random import random
from .generator import Generator


class Boolean(Generator):
    def __init__(self, probability_of_true=0.5, *args, **kwargs):
        """
        Create a boolean generator that will result in a boolean value
        :param probability_of_true: The probability of generating a
        True value. From 0-1.
        """
        super().__init__(*args, **kwargs)
        self.prob_of_true = probability_of_true

    def _one(self) -> bool:
        if random() <= self.prob_of_true:
            return True
        else:
            return False
