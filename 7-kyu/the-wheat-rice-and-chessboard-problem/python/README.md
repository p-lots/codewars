I assume most of you are familiar with the ancient legend of the rice (but I see wikipedia suggests [wheat](https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem), for some reason) problem, but a quick recap for you: a young man asks as a compensation only `1` grain of rice for the first square, `2` grains for the second, `4` for the third, `8` for the fourth and so on, always doubling the previous.

Your task is pretty straightforward (but not necessarily easy): given an amount of grains, you need to return up to which square of the chessboard one should count in order to get at least as many.

As usual, a few examples might be way better than thousands of words from me:

```javascript
squaresNeeded(0) === 0
squaresNeeded(1) === 1
squaresNeeded(2) === 2
squaresNeeded(3) === 2
squaresNeeded(4) === 3
```
```cpp
squaresNeeded(0) == 0
squaresNeeded(1) == 1
squaresNeeded(2) == 2
squaresNeeded(3) == 2
squaresNeeded(4) == 3
```
```python
squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3
```
```ruby
squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3
```
```crystal
squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3
```
```csharp
SquaresNeeded(0) == 0
SquaresNeeded(1) == 1
SquaresNeeded(2) == 2
SquaresNeeded(3) == 2
SquaresNeeded(4) == 3
```
```c
squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3
```
```groovy
Kata.squaresNeeded(0) == 0
Kata.squaresNeeded(1) == 1
Kata.squaresNeeded(2) == 2
Kata.squaresNeeded(3) == 2
Kata.squaresNeeded(4) == 3
```
```typescript
squaresNeeded(0) === 0
squaresNeeded(1) === 1
squaresNeeded(2) === 2
squaresNeeded(3) === 2
squaresNeeded(4) === 3
```
```julia
squaresneeded(0) == 0
squaresneeded(1) == 1
squaresneeded(2) == 2
squaresneeded(3) == 2
squaresneeded(4) == 3
```

Input is always going to be valid/reasonable: ie: a non negative number; extra cookie for *not* using a loop to compute square-by-square (at least not directly) and instead trying a smarter approach [hint: some peculiar operator]; a trick converting the number might also work: impress me!
