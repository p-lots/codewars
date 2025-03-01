**Task**
Given a list of values, return a list with each value replaced with the empty value of the same type.

**More explicitly**

- Replace integers `(e.g. 1, 3)`, whose type is int, with `0`
- Replace floats `(e.g. 3.14, 2.17)`, whose type is float, with `0.0`
- Replace strings `(e.g. "abcde", "x")`, whose type is str, with `""`
- Replace booleans `(True, False)`, whose type is bool, with `False`
- Replace lists `(e.g. [1, "a", 5], [[4]])`, whose type is list, with `[]`
- Replace tuples `(e.g. (1,9,0), (2,))`, whose type is tuple, with `()`
- Replace dictionaries `(e.g. {29: 11, 24: 63})`, whose type is dictionary, with `{}`
- Replace sets `(e.g. {0,"a"}, {"b"})`, whose type is set, with `set()`
    - Caution: Python interprets `{}` as the empty dictionary, **not** the empty set.
- `None`, whose type is NoneType, is preserved as None

**Examples**
```
[1, 2, 3] ➞ [0, 0, 0]

[7, 3.14, "cat"] ➞ [0, 0.0, ""]

[[1, 2, 3], (1,2,3), {1,2,3}] ➞ [[], (), set()]

[[7, 3.14, "cat"]] ➞ [[]]

[{}] ➞ [{}]

[None] ➞ [None]
```
**Notes**
`None` has the special `NoneType` all for itself.