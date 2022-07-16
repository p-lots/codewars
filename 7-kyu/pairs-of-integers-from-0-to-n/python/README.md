Write a function `generatePairs` (Javascript) / `generate_pairs` (Python / Ruby) that accepts an integer argument `n` and generates an array containing the pairs of integers `[a, b]` that satisfy the following conditions:
```
0 <= a <= b <= n
```

The pairs should be sorted by increasing values of `a` then increasing values of `b`.

For example, 

``` javascript
generatePairs(2) should return
[ [0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2] ]
```

``` python
generate_pairs(2) should return
[ [0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2] ]
```

``` ruby
generate_pairs(2) should return
[ [0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2] ]
```

```julia
generatepairs(2) # should return 
[ (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2) ]
```

```cobol
      generatePairs(2) 
      --> result = [ [0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2] ]
```