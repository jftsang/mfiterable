# MFIterable

J. M. F. Tsang ([j.m.f.tsang@cantab.net](j.m.f.tsang@cantab.net))

---

`MFIterable` is an `Iterable` that provides `.map` and `.filter` methods 
for JavaScript-style chaining.

Example:
```python
from mfiterable import MFIterable

lst = (MFIterable(range(10))
       .filter(lambda x : x % 2 == 0)
       .map(lambda x: x ** 2 if x != 4 else None)
       .drop_nones()
       .to_list()
       )  # [0, 4, 36, 64]
```
