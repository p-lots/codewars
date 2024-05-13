Rick wants a faster way to get the product of the largest pair in an array. Your task is to create a <b>performant</b> solution to find the product of the largest two integers in a <b>unique</b> array of <b>positive</b> numbers.<br> <u>All inputs will be valid.</u><br>
<u>Passing [2, 6, 3] should return 18, the product of [6, 3].</u>

```Disclaimer: only accepts solutions that are faster than his, which has a running time O(nlogn).``` 

```ruby
max_product([2, 1, 5, 0, 4, 3])              # => 20
max_product([7, 8, 9])                       # => 72
max_product([33, 231, 454, 11, 9, 99, 57])   # => 104874
```
```javascript
maxProduct([2, 1, 5, 0, 4, 3])              // 20
maxProduct([7, 8, 9])                       // 72
maxProduct([33, 231, 454, 11, 9, 99, 57])   // 104874
```
```python
max_product([2, 1, 5, 0, 4, 3])              # => 20
max_product([7, 8, 9])                       # => 72
max_product([33, 231, 454, 11, 9, 99, 57])   # => 104874
```
```csharp
Kata.MaxProduct(new int[] { 2, 1, 5, 0, 4, 3 });              // 20
Kata.MaxProduct(new int[] { 7, 8, 9 })     ;                  // 72
Kata.MaxProduct(new int[] { 33, 231, 454, 11, 9, 99, 57 });   // 104874
```