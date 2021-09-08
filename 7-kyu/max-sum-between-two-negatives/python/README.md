You have a list of integers. The task is to return the maximum sum of the elements located between two negative elements, or `-1`, `Nothing`, or a similar empty value, if there is no such sum. No negative element should be present in this sum. 

Example:

```python
[4, -1, 6, -2, 3, 5, -7, 7] -> 8
     ^      ^         ^
```

Not `14`, because `-2` is between `-1` and `-7`, and not `6` but `8`, because `8` is bigger.