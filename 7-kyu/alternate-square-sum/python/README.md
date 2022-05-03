Write a method `alternate_sq_sum()` (JS: `alternateSqSum` ) that takes an array of integers as input and finds the sum of squares of the elements at even positions (*i.e.,* 2nd, 4th, *etc.*) plus the sum of the rest of the elements at odd position.

<h2 style="color:red">NOTE:<h2>
<p style="color:yellow">The values at even *position* need to be squared. For a language with zero-based indices, this will occur at oddly-indexed locations. For instance, in Python, the values at indices 1, 3, 5, *etc.* should be squared because these are the second, fourth, and sixth positions in the list.
<h2 style="color:lightGreen">For Example:</h2>

```ruby
alternate_sq_sum([11, 12, 13, 14, 15]) #should return 379
```
```javascript
alternateSqSum([11, 12, 13, 14, 15]) // should return 379
```
```python
alternate_sq_sum([11, 12, 13, 14, 15]) #should return 379
```
```haskell
alternateSqSum [11..15] `shouldBe` Just 379
alternateSqSum [] `shouldBe` Nothing
```
```java
alternateSqSum(new int[] {11, 12, 13, 14, 15}) // should return 379
```

<h2 style="color:cyan">Explanation:</h2>

Elements at indices 0, 2, 4 are 11, 13, 15 and they are at odd positions as 11 is at position #1, 13 is at position #3 and 15 at #5.

Elements at indices 1, 3 are 12 and 14 and they are at even position.
So we need to add 11, 13, 15 as they are and square of 12 and 14

--> 11 + 13 + 15 + 12^2 + 14^2<br>
  = 11 + 13 + 15 + 144 + 196<br>
  = 379

<p style="color:lightBlue">For empty arrays, result should be 0 (zero) (except for Haskell).</p>