## Task

Write a function that checks if two non-negative integers make an "interlocking binary pair".

## Interlock ?

* numbers can be interlocked if their binary representations have no `1`'s in the same place
* comparisons are made by bit position, starting from right to left (see the examples below)
* when representations are of different lengths, the unmatched left-most bits are ignored

## Examples
1) `a = 9`, `b = 4`

   Stacking representations shows how they can interlock.
   ```
    9    1001
    4     100
   ```
   Here, no `1`'s share any position, so the function returns `true`.<br><br>
2) `a = 3`, `b = 6`

   These representations do not interlock.
   ```
    3      11
    6     110
   ```
   Finding they both have a `1` in the same position, the function returns `false`.

## Input

Two non-negative integers.

## Output

Boolean `true` or `false` whether or not these integers are interlockable.

## Enjoy!

...and please consider one of the following kata to solve next:
* [Setting Places for the Dead](https://www.codewars.com/kata/6646c0c08b97085ca216d346)
* [Four Letter Words ~ Anagrams](https://www.codewars.com/kata/5cb5ebc403c3ff477840393a/discuss#66ed61991c50f3905fb9adbd)
* [Shuffle an Integer](https://www.codewars.com/kata/6467a353f81b1f0031004eb8/python)
* [Minimum Percentage of Visitors that Ate All Foods](https://www.codewars.com/kata/657e578bdc80170abd4dca79)
* [The Jumbler](https://www.codewars.com/kata/69269262ced9e95dc63abd1e/c)
* [Do They Agree?](https://www.codewars.com/kata/6a2deeb1a8b6a4b0a80430af)
* [Find the Liar](https://www.codewars.com/kata/6a3a9918dfc9a3213d103571/c)
* [Is Sator Square?](https://www.codewars.com/kata/5cb7baa989b1c50014a53333)
* [Playing With Toy Blocks ~ Can you build a 4x4 square?](https://www.codewars.com/kata/5cab471da732b30018968071)
* [Four Letter Words ~ Mutations](https://www.codewars.com/kata/5cb5eb1f03c3ff4778402099)
* [Crossword Puzzle! (2x2)](https://www.codewars.com/kata/5c658c2dd1574532507da30b)