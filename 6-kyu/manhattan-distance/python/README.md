The distance formula can be used to find the distance between two points. What if we were trying to walk from point **A** to point **B**, but there were buildings in the way? We would need some other formula..but which?


### Manhattan Distance

[Manhattan distance](http://en.wikipedia.org/wiki/Manhattan_distance) is the distance between two points in a grid (like the grid-like street geography of the New York borough of Manhattan) calculated by only taking a vertical and/or horizontal path.

Complete the function that accepts two points and returns the Manhattan Distance between the two points.

The points are arrays containing the `x` and `y` coordinate in the grid. You can think of `x` as the row in the grid, and `y` as the column.


### Examples

```javascript
manhattanDistance( [1, 1], [1, 1] ) // => returns 0
manhattanDistance( [5, 4], [3, 2] ) // => returns 4
manhattanDistance( [1, 1], [0, 3] ) // => returns 3
```
```ruby
manhattan_distance( [1, 1], [1, 1] ) # => returns 0
manhattan_distance( [5, 4], [3, 2] ) # => returns 4
manhattan_distance( [1, 1], [0, 3] ) # => returns 3
```
```python
manhattan_distance( [1, 1], [1, 1] ) # => returns 0
manhattan_distance( [5, 4], [3, 2] ) # => returns 4
manhattan_distance( [1, 1], [0, 3] ) # => returns 3
```
```c
manhattan_distance( {1, 1}, {1, 1} ); // => returns 0
manhattan_distance( {5, 4}, {3, 2} ); // => returns 4
manhattan_distance( {1, 1}, {0, 3} ); // => returns 3
```
```prolog
manhattan_distance( [1, 1], [1, 1], 0 ).
manhattan_distance( [5, 4], [3, 2], 4 ).
manhattan_distance( [1, 1], [0, 3], 3 ).
```
```cfml
manhattanDistance( [1, 1], [1, 1] ) // => returns 0
manhattanDistance( [5, 4], [3, 2] ) // => returns 4
manhattanDistance( [1, 1], [0, 3] ) // => returns 3
```
```typescript
manhattanDistance( [1, 1], [1, 1] ) // => returns 0
manhattanDistance( [5, 4], [3, 2] ) // => returns 4
manhattanDistance( [1, 1], [0, 3] ) // => returns 3
```
```coffeescript
manhattanDistance( [1, 1], [1, 1] ) // => returns 0
manhattanDistance( [5, 4], [3, 2] ) // => returns 4
manhattanDistance( [1, 1], [0, 3] ) // => returns 3
```
