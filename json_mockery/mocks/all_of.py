from typing import Union, List, Tuple
from random import shuffle as shuffler
from .generator import Generator


class AllOf(Generator):
    def __init__(self, *args: any, shuffle=False, **kwargs):
        super().__init__(**kwargs)
        self.options: List[any] = [*args]
        self.working_copy: List[any] = [*self.options]
        self.shuffle = shuffle

        if self.shuffle:
            shuffler(self.working_copy)

    def _one(self) -> any:
        return self.options.pop()

    def add(self, option: any):
        self.options.append(option)

    def exhausted(self) -> bool:
        result = len(self.options) == 0

        # auto-reset
        if result:
            self.working_copy = [*self.options]
            if self.shuffle:
                shuffler(self.working_copy)

        return result
