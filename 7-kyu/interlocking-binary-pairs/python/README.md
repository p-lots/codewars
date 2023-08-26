# Task

Write a function that checks if two non-negative integers make an "interlocking binary pair".

<br>


# Interlock ?
* numbers can be interlocked if their binary representations have no `1`'s in the same place
* comparisons are made by bit position, starting from right to left (see the examples below)
* when representations are of different lengths, the unmatched left-most bits are ignored

<br>

# Examples

1) `a = 9`, `b = 4`

Stacking representations shows how they can interlock.
   ```
    9    1001
    4     100
   ```
Here, no `1`'s share any position, so the function returns `true`.

2) `a = 3`, `b = 6`

These representations do not interlock.
   ```
    3      11
    6     110
   ```
Finding they both have a `1` in the same position, the function returns `false`.

<br>

# Input

Two non-negative integers.

# Output

Boolean `true` or `false` whether or not these integers are interlockable.

<br>

# Enjoy!

Consider one of the following kata to solve next:
* [Crossword Puzzle! (2x2)](https://www.codewars.com/kata/5c658c2dd1574532507da30b)
* [Four Letter Words ~ Mutations](https://www.codewars.com/kata/5cb5eb1f03c3ff4778402099)
* [Is Sator Square?](https://www.codewars.com/kata/5cb7baa989b1c50014a53333)
* [Playing With Toy Blocks ~ Can you build a 4x4 square?](https://www.codewars.com/kata/5cab471da732b30018968071)

<br>

# Nota Bene:

This kata is accepting of translations for any languages other than: Java, JavaScript, CoffeeScript, TypeScript, Go, Groovy, Julia, Dart, and Kotlin; as those are currently underway by the author. Thank you!