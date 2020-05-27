from typing import Union, List, Tuple
from random import random
from .generator import Generator


class OneOf(Generator):
    def __init__(self, *args: Union[any, Tuple[any, float]], **kwargs):
        super().__init__(**kwargs)
        self.choices: List[Tuple[Union[any, Generator], Union[None, float]]] = []
        self.prob_sum = 0
        self.cache = None

        for arg in args:
            if isinstance(arg, (tuple, list)):
                self.add(arg[0], arg[1])
            else:
                self.add(arg)

    def _one(self) -> any:
        if self.cache is None:
            choices = self.choices[:]

            none_count = 0
            for choice in choices:
                if choice[1] is None:
                    none_count += 1

            if none_count != 0:
                per_item = (1 - self.prob_sum) / none_count
                for i in range(len(choices)):
                    choices[i] = (choices[i][0], per_item)

            choices.sort(key=lambda x: x[1], reverse=True)

            # make cumulative
            sum_ = 0
            for i in range(len(choices)):
                sum_ += choices[i][1]
                choices[i] = (choices[i][0], sum_)

            self.cache = choices

        val = random()
        for choice in self.cache:
            if val <= choice[1]:
                if isinstance(choice[0], Generator):
                    return choice[0].one()
                else:
                    return choice[0]

    def add(self, choice: Union[any, Generator], probability: float = None):
        self.cache = None
        if probability is not None and self.prob_sum + probability > 1:
            raise ValueError("The sum of probabilities across all choices cannot be greater than 1")
        else:
            if probability is not None:
                self.prob_sum += probability
            self.choices.append((choice, probability))
