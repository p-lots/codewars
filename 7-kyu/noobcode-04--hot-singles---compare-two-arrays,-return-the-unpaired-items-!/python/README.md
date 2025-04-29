Write a function that takes two array arguments, and returns a new array populated with the elements **that appear in either array, but not in both. Elements should only appear once in the returned array**. 

The order of the elements in the result should follow what appears in the first array, then the second one.


## Examples
~~~if-not:haskell
```
[1, 2, 3, 3], [3, 2, 1, 4, 5] --> [4, 5]

["tartar", "blanket", "cinnamon"], ["cinnamon", "blanket", "domino"] --> ["tartar", "domino"]

[77, "ciao"], [78, 42, "ciao"] --> [77, 78, 42]

[1, 2, 3, 3], [3, 2, 1, 4, 5, 4] --> [4,5]

[1, 2, 3] , [3, 3, 2, 1] --> []
```
~~~
~~~if:haskell
```haskell
>>> hotSingles [1, 2, 3, 3] [3, 2, 1, 4, 5]
[4,5]
>>> hotSingles ["tartar", "blanket", "cinnamon"] ["cinnamon", "blanket", "domino"]
["tartar","domino"]
>>> hotSingles [77] [78, 42]
[77,78,42]
>>> hotSingles [1, 2, 3, 3] [3, 2, 1, 4, 5, 4]
[4,5]
>>> hotSingles [1, 2, 3] [3, 3, 2, 1]
[]
```
~~~

SPECIAL THANKS: @JulianKolbe !