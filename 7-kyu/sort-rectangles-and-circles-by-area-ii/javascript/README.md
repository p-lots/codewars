In this kata you will be given a sequence of the dimensions of rectangles ( sequence with width and length ) and circles ( radius - just a number ).  
Your task is to return a new sequence of dimensions, sorted ascending by area.

For example,

```javascript
const array = [ [4.23, 6.43], 1.23, 3.444, [1.342, 3.212] ]; // [ rectangle, circle, circle, rectangle ]
sortByArea(array) => [ [ 1.342, 3.212 ], 1.23, [ 4.23, 6.43 ], 3.444 ]
```
```python
seq = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ] # [ rectangle, circle, circle, rectangle ]
sort_by_area(seq) => [ ( 1.342, 3.212 ), 1.23, ( 4.23, 6.43 ), 3.444 ]
```
```ruby
seq = [ [4.23, 6.43], 1.23, 3.444, [1.342, 3.212] ] # [ rectangle, circle, circle, rectangle ]
sort_by_area(seq) => [ [1.342, 3.212], 1.23, [4.23, 6.43], 3.444 ]
```
```haskell
list = [ Rectangle 4.23 6.43, Circle 1.23, Circle 3.444, Rectangle 1.342 3.212 ]
sortByArea list -> [ Rectangle 1.342 3.212, Circle 1.23, Rectangle 4.23 6.43, Circle 3.444 ]
```
```c
seq = { {4.23, 6.43}, {1.23, 0.0}, {3.444, 0.0}, {1.342, 3.212} } // { rectangle, circle, circle, rectangle }
sort_by_area(seq) => { {1.342, 3.212}, {1.23, 0.0}, {4.23, 6.43}, {3.444, 0.0} }
```
```cpp
seq = { {4.23, 6.43}, {1.23, 0}, {3.444, 0}, {1.342, 3.212} } // { rectangle, circle, circle, rectangle }
sort_by_area(seq) => { {1.342, 3.212}, {1.23, 0}, {4.23, 6.43}, {3.444, 0} }
```
```ocaml
shapes = [ Rectangle (4.23, 6.43); Circle 1.23; Circle 3.444; Rectangle (1.342, 3.212) ]
sort_by_area shapes -> [ Rectangle (1.342, 3.212); Circle 1.23; Rectangle (4.23, 6.43); Circle 3.444 ]
```
```factor
{ { 4.23 6.43 } 1.23 3.444 { 1.342 3.212 } } ! { rectangle circle circle rectangle }
sort-by-area -> { { 1.342 3.212 } 1.23 { 4.23 6.43 } 3.444 }
```
```lua
seq = { {4.23, 6.43}, 1.23, 3.444, {1.342, 3.212} } -- { rectangle, circle, circle, rectangle }
sort_by_area(seq) --> { {1.342, 3.212}, 1.23, {4.23, 6.43}, 3.444 }
```
```rust
seq = &[ Either::Left((4.23, 6.43)), Either::Right(1.23), Either::Right(3.444), Either::Left((1.342, 3.212)) ] // ( rectangle, circle, circle, rectangle )

sort_by_area(seq) => &[ Either::Left((1.342, 3.212)), Either::Right(1.23), Either::Left((4.23, 6.43)), Either::Right(3.444) ];
```

This kata inspired by [Sort rectangles and circles by area](https://www.codewars.com/kata/sort-rectangles-and-circles-by-area/).