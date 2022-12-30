from typing import Iterable, TypeVar, Iterator, Callable, List

T = TypeVar('T')
V = TypeVar('V')


class MFIterable(Iterable[T]):
    """Iterable that provides map and filter methods for chaining."""
    def __init__(self, it: Iterable[T]):
        self.it = it

    def __iter__(self) -> Iterator[T]:
        return iter(self.it)

    def map(self, f: Callable[[T], V]) -> 'MFIterable[V]':
        return MFIterable(map(f, self.it))

    def filter(self, pred: Callable[[T], bool]) -> 'MFIterable[T]':
        return MFIterable(filter(pred, self.it))

    def drop_nones(self) -> 'MFIterable[T]':
        return self.filter(lambda x: x is not None)

    def to_list(self) -> List[T]:
        return list(self)
