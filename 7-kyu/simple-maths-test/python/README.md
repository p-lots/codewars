Create a function which checks a number for three different properties.

- is the number prime?
- is the number even?
- is the number a multiple of 10?

Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses `data Property`.

### Examples
```javascript
numberProperty(7)  // ==> [true,  false, false] 
numberProperty(10) // ==> [false, true,  true] 
```
```ruby
number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true] 
```
```python
number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true] 
```
```haskell
numberProperty 7  `shouldBe` Property True  False False
numberProperty 10 `shouldBe` Property False True  True
```
```csharp
Kata.NumberProperty(7)  => new bool[] {true, false, false}
Kata.NumberProperty(10) => new bool[] {false, true, true}
```
```java
SimpleMath.numberProperty(7)  => new boolean[] {true, false, false}
SimpleMath.numberProperty(10) => new boolean[] {false, true, true}
```
The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:

```javascript
numberProperty(-7)  // ==> [false, false, false] 
numberProperty(-10) // ==> [false, true,  true] 
```
```ruby
number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true] 
```
```python
number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true] 
```
```haskell
numberProperty (-7)  `shouldBe` Property False False False
numberProperty (-10) `shouldBe` Property False True  True
```
```csharp
Kata.NumberProperty(-7)  => new bool[] {false, false, false}
Kata.NumberProperty(-10) => new bool[] {false, true, true}
```
```java
SimpleMath.numberProperty(-7)  => new boolean[] {false, false, false}
SimpleMath.numberProperty(-10) => new boolean[] {false, true, true}
```