## Task

Write a function which accepts a sequence of unique integers as argument and returns a 32-bit integer such that the integer, in its binary representation has `1` at only those indexes (counted from right) which are in the sequence.

## Examples

```javascript
sortByBit([0, 1]) // Returns integer 3
sortByBit([1, 2, 0, 4]) // Returns integer 23
```
```python
sort_by_bit([0, 1]) # Returns integer 3
sort_by_bit([1, 2, 0, 4]) # Returns integer 23
```
```rust
sort_by_bit(&[0, 1]) // Returns integer 3
sort_by_bit(&[1, 2, 0, 4]) // Returns integer 23  
``` 
```julia
sortbybit([0, 1]) # Returns integer 3
sortbybit([1, 2, 0, 4]) # Returns integer 23
```          
&nbsp;
```
Because 23 in binary is:                     
                               
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 1      
                                          . . . . . 5 4 3 2 1 0  <--- indices     
                                                      |   | | |                       
                                                      |   | | |                       
                            these bits are 1 due to the corresponding indices in the given array
```

**FAQ**: The function name contains `sort` as it simulates [radix sort](https://en.wikipedia.org/wiki/Radix_sort).