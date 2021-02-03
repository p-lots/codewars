Create a function ```isDivisible(n,...)``` that checks if the first argument n is divisible by all other arguments (return true if no other arguments)

Example:
```javascript
isDivisible(6,1,3)--> true because 6 is divisible by 1 and 3
isDivisible(12,2)--> true because 12 is divisible by 2
isDivisible(100,5,4,10,25,20)--> true
isDivisible(12,7)--> false because 12 is not divisible by 7
```
```haskell
isDivisible   3 [1,3]          `shouldBe` True
isDivisible  12 [2]            `shouldBe` True
isDivisible 100 [5,4,10,25,20] `shouldBe` True
isDivisible  12 [7]            `shouldBe` False
```
```c
Assert.AreEqual(false, Kata.IsDivisible(3,3,4));
Assert.AreEqual(true, Kata.IsDivisible(12, 3, 4));
```


This kata is following kata: http://www.codewars.com/kata/is-n-divisible-by-x-and-y
