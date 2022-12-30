from typing import Iterable, TypeVar, Iterator, Callable, List

_T = TypeVar('_T')
_V = TypeVar('_V')


class MFIterable(Iterable[_T]):
    """Iterable that provides map and filter methods for chaining."""
    def __init__(self, it: Iterable[_T]):
        self.it = it

    def __iter__(self) -> Iterator[_T]:
        return iter(self.it)

    def map(self, f: Callable[[_T], _V]) -> 'MFIterable[_V]':
        return MFIterable(map(f, self.it))

    def filter(self, pred: Callable[[_T], bool]) -> 'MFIterable[_T]':
        return MFIterable(filter(pred, self.it))

    def drop_nones(self) -> 'MFIterable[_T]':
        return self.filter(lambda x: x is not None)

    def to_list(self) -> List[_T]:
        return list(self)
