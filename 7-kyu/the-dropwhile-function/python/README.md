Yet another staple for the functional programmer. You have a sequence of values and some predicate for those values. You want to remove the longest prefix of elements such that the predicate is true for each element. We'll call this the dropWhile function. It accepts two arguments. The first is the sequence of values, and the second is the predicate function. The function does not change the value of the original sequence. 

```python
def isEven(num):
  return num % 2 == 0

arr = [2,4,6,8,1,2,5,4,3,2]

dropWhile(arr, isEven) == [1,2,5,4,3,2] # True
```
```javascript
function isEven(num) {
  return num % 2 === 0;
}
var seq = [2,4,6,8,1,2,5,4,3,2];

dropWhile(seq, isEven) // -> [1,2,5,4,3,2]
```
```haskell
dropWhile [2,4,6,8,1,2,5,4,3,2] even -- -> [1,2,5,4,3,2]
```
```cpp
auto isEven = [](int value) -> bool { return abs(value) % 2 == 0; };

dropWhile({ 2, 4, 6, 8, 1, 2, 5, 4, 3, 2 }, isEven) // -> { 1, 2, 5, 4, 3, 2 }
```
```csharp
Func<int, bool> isEven = (value) => value % 2 == 0;

dropWhile(new int[] { 2, 4, 6, 8, 1, 2, 5, 4, 3, 2 }, isEven) // -> { 1, 2, 5, 4, 3, 2 }
```
```lambdacalc
drop-while [2,4,6,8,1,2,5,4,3,2] even  -->  [1,2,5,4,3,2]
```
```lua
local function is_even(x)
  return x%2==0
end

drop_while({2,4,6,8,1,2,5,4,3,2}, is_even)  -->  [1,2,5,4,3,2]
```
```ocaml
let is_even n = n mod 2 = 0 in
drop_while [2; 4; 6; 8; 1; 2; 5; 4; 3; 2] is_even
  (* -> [1; 2; 5; 4; 3; 2] *)
```

Your task is to implement the dropWhile function. If you've got a [span function](http://www.codewars.com/kata/the-span-function) lying around, this is a one-liner! Alternatively, if you have a [takeWhile function](http://www.codewars.com/kata/the-takewhile-function) on your hands, then combined with the dropWhile function, you can implement the span function in one line. This is the beauty of functional programming: there are a whole host of useful functions, many of which can be implemented in terms of each other.

~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` and deconstructor `foldl` for your `List` encoding  
export constructors `False, True` for your `Boolean` encoding  
~~~