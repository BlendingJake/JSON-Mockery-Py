from random import random
from .generator import Generator


class Optional(Generator):
    def __init__(self, gen: Generator, probability=0.5, *args, **kwargs):
        """
        Create an optional generator that will result in Nothing a certain
        percentage of the time.
        :param gen: The generator that will be used if a value is being produced
        :param probability: The probability of Nothing. From 0-1.
        """
        super().__init__(*args, **kwargs)
        self.generator = gen
        self.probability = probability

    def _one(self):
        if random() <= self.probability:
            return self.Nothing
        else:
            return self.generator.one()
