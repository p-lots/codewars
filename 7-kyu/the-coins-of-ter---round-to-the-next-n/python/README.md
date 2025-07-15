<div style="border:1px solid; padding:1ex;">Inspired by <a href="/kata/55d1d6d5955ec6365400006d">Round to the next 5</a>.
<strong>Warning!</strong> This kata contains spoilers on the mentioned one. Solve that one first!</div>

# The Coins of Ter

Ter is a small country, located between Brelnam and the Orange juice ocean. It uses many different coins and bills for payment. However, one day, the leaders of Ter decide that there are too many small coins. Therefore, they ban the small coins. But no one knows _which_ coins they'll ban, so they ask you to provide a tool that can recalculate a price. After all, if one does not have a 1 Terrek bill and can only give a 2 Terrek bill, one needs to adjust the oddly priced items.

# Task

Write a function `adjust`, that takes a two integers: the lowest currency unit that's still allowed, and the price/debt that needs to get adjusted. All prices are going up, and debts are remitted. The lowest currency will always be positive.

In other words:`adjust` takes two integers, `b` and `n`, and returns the smallest number `k`, such that `n <= k` and `k % b == 0 `.

# Examples

```haskell
adjust 3 0    `shouldBe` 0
adjust 3 1    `shouldBe` 3
adjust 3 (-2) `shouldBe` 0
adjust 3 (-4) `shouldBe` (-3)
adjust 3 3    `shouldBe` 3
adjust 6 3    `shouldBe` 6
adjust 7 3    `shouldBe` 9
```
```javascript
adjust( 3, 0 ) ===  0
adjust( 3, 1 ) ===  3
adjust( 3, -2) ===  0
adjust( 3, -4) === -3
adjust( 3, 3 ) ===  3
adjust( 3, 6 ) ===  6
adjust( 3, 7 ) ===  9
```
```coffeescript
adjust( 3, 0 ) ===  0
adjust( 3, 1 ) ===  3
adjust( 3, -2) ===  0
adjust( 3, -4) === -3
adjust( 3, 3 ) ===  3
adjust( 3, 6 ) ===  6
adjust( 3, 7 ) ===  9
```
```python
adjust( 3, 0 ) ==  0
adjust( 3, 1 ) ==  3
adjust( 3, -2) ==  0
adjust( 3, -4) == -3
adjust( 3, 3 ) ==  3
adjust( 3, 6 ) ==  6
adjust( 3, 7 ) ==  9
```
```ruby
adjust( 3, 0 ) ==  0
adjust( 3, 1 ) ==  3
adjust( 3, -2) ==  0
adjust( 3, -4) == -3
adjust( 3, 3 ) ==  3
adjust( 3, 6 ) ==  6
adjust( 3, 7 ) ==  9
```

<div style="border:1px solid; padding:1ex;">
<strong>Translator notice:</strong> Make sure that you provide about the same random tests, so that a user can get feedback during "Run tests", and not only during "Submit".</div>