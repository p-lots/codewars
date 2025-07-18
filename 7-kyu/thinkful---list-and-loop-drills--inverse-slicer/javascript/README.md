You're familiar with [list slicing](https://docs.python.org/3/library/functions.html#slice) in Python and know, for example, that:

```python
>>> ages = [12, 14, 63, 72, 55, 24]
>>> ages[2:4]
[63, 72]
>>> ages[2:]
[63, 72, 55, 24]
>>> ages[:3]
[12, 14, 63]
```

Write a function `inverse_slice` that takes three arguments: a list `items`, an integer `a` and an integer `b`. The function should return a new list with the slice specified by `items[a:b]` __*excluded*__.

For example:

```python
>>>inverse_slice([12, 14, 63, 72, 55, 24], 2, 4)
[12, 14, 55, 24]
```
```rust
inverse_slice(&[12, 14, 63, 72, 55, 24], 2, 4) == [12, 14, 55, 24]
```

Input domain:
- `items` will always be a valid sequence.
- `b` will always be greater than `a`.
- `a` will always be greater than or equal to zero.
- `a` will always be less than the length of `items`.
- `b` may be greater than the length of `items`.

```if:cobol
#### Note for COBOL:
Remember COBOL's tables use 1-based indexing, so `a` and `b` will always be superior or equal to 1, and indexes need to be shifted by 1 in comparison with other languages:

     InverseSlice [12, 14, 63, 72, 55, 24], 3, 5 => [12, 14, 55, 24]
```