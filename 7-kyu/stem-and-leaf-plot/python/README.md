A stem-and-leaf plot groups data points that have the same leading digit, resembling a histogram. For example, for the input `[11, 35, 14, 9, 39, 23, 35]`, it might look something like this:

```
stem | leaf
-----------
  0  | 9
  1  | 1 4
  2  | 3
  3  | 5 5 9
```

Some important things to notice: 
  * Any single-digit number, such as `9`, has `0` as its stem; 
  * The leaves are presented in ascending order; 
  * Leaves can be repeated (as with the two 5's in the last row).

Create a function called `stem_and_leaf` that, given a list of integers `i` as input (`0 <= i <= 99`), returns a Python dictionary containing a stem-and-leaf plot. Each key of the dictionary should be a stem and each value should be a list of leaves, following the format above.

For the example above, the output would be:

```
{0: [9], 1: [1, 4], 2: [3], 3: [5, 5, 9]}
```