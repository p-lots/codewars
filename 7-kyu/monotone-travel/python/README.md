# Story
Peter lives on a hill, and he always moans about the way to his home. "It's always just up. I never get a rest". But you're pretty sure that at least at one point Peter's altitude doesn't rise, but fall. To get him, you use a nefarious plan: you attach an altimeter to his backpack and you read the data from his way back at the next day.

# Task
You're given a list of compareable elements:

```haskell
Ord a => [a]
```
```ruby
heights = [Integers or Floats]
```
```python
heights = [Integers or Floats]
```
```javascript
heights = [h1, h2, h3, …, hn]
```
```csharp
heights = new int[0 ... 100]
```

Your job is to check whether for any `x` all successors are greater or equal to `x`.

```haskell
isMonotone [1,2,3] == True
isMonotone [1,1,2] == True
isMonotone [1]     == True
isMonotone [3,2,2] == False
```
```ruby
is_monotone([1,2,3]) == True
is_monotone([1,1,2]) == True
is_monotone([1])     == True
is_monotone([3,2,1]) == False
is_monotone([3,2,2]) == False
```
```python
is_monotone([1,2,3]) == True
is_monotone([1,1,2]) == True
is_monotone([1])     == True
is_monotone([3,2,1]) == False
is_monotone([3,2,2]) == False
```
```javascript
isMonotone([1,2,3]) == true
isMonotone([1,1,2]) == true
isMonotone([1])     == true
isMonotone([3,2,1]) == false
isMonotone([3,2,2]) == false
```
```csharp
Kata.IsMonotone(new int[] {1,2,3}) => true
Kata.IsMonotone(new int[] {1,1,2}) => true
Kata.IsMonotone(new int[] {1})     => true
Kata.IsMonotone(new int[] {3,2,1}) => false
Kata.IsMonotone(new int[] {3,2,2}) => false
```
If the list is empty, Peter has probably removed your altimeter, so we cannot prove him wrong and he's still right:
```haskell
isMonotone []      == True
```
```ruby
isMonotone([])     == True
```
```python
is_monotone([])     == True
```
```javascript
isMonotone([])     == True
```
```csharp
Kata.IsMonotone(new int[] {}) => true
```
Such a sequence is also called *monotone* or [*monotonic* sequence](https://en.wikipedia.org/wiki/Monotonic_function), hence the name `isMonotone`.