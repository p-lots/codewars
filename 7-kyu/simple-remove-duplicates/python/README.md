In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

```haskell
solve [3, 4, 4, 3, 6, 3]-- => [4, 6, 3]
-- Remove the 3's at indices 0 and 3
-- followed by removing a 4 at index 1
```
```purescript
-- Remove the 3's at indices 0 and 3
-- followed by removing a 4 at index 1
solve (3 : 4 : 4 : 3 : 6 : 3 : Nil) -- => 4 : 6 : 3 : Nil
```
```javascript
// Remove the 3's at indices 0 and 3
// followed by removing a 4 at index 1
solve([3, 4, 4, 3, 6, 3]); // => [4, 6, 3]
```
```python
# Remove the 3's at indices 0 and 3
# followed by removing a 4 at index 1
solve([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]
```
```ruby
# Remove the 3's at indices 0 and 3
# followed by removing a 4 at index 1
solve ([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]
```

More examples can be found in the test cases. 

Good luck!