Given: a sequence of different type of values (number, string, boolean). You should return an object with a separate properties for each of types presented in input. Each property should contain an array of corresponding values.

- keep order of values like in input array
- if type is not presented in input, no corresponding property are expected  


So, for this input:

```javascript
['a', 1, 2, false, 'b']
```

```python
['a', 1, 2, False, 'b']
```

expected output is:
```javascript
{
  number: [1, 2],
  string: ['a', 'b'],
  boolean: [false]
}
```

```python
{
  int: [1, 2],
  str: ['a', 'b'],
  bool: [False]
}
```