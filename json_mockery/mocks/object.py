from typing import Union, Dict, Tuple
from .generator import Generator

JSONValue = Union[None, str, int, float, list, dict, Generator]
JSONKey = Union[str, Generator]


class Object(Generator):
    def __init__(self, *args: Union[Tuple[JSONKey, JSONValue], Generator],
                 nullable=False, null_probability=0.5, **kwargs: JSONValue):
        """
        Create a new Object generator
        :param args: Can be a list of tuples of (key, value) or exactly two arguments, each of
        which are generators, where the first generator is used for the keys and the second
        for the values.
        :param kwargs: Key -> Value mapping
        """
        super().__init__(nullable, null_probability)
        self.key_values: Dict[
            Union[str, Generator],
            Union[str, int, float, list, dict, Generator]
        ] = {**kwargs}

        if len(args) == 2 and all(isinstance(arg, Generator) for arg in args):
            while not args[0].exhausted():
                self.add(args[0].one(), args[1].one())
        else:
            for k, v in args:
                self.add(k, v)

    def _one(self) -> dict:
        out = {}
        for k, v in self.key_values.items():
            if isinstance(v, Generator):
                value = v.one()
            else:
                value = v

            if value is not self.Nothing:
                if isinstance(k, Generator):
                    key = k.one()
                else:
                    key = k

                if key is not self.Nothing:
                    out[key] = value

        return out

    def add(self, key: JSONKey, value: JSONValue) -> 'Object':
        self.key_values[key] = value
        return self
