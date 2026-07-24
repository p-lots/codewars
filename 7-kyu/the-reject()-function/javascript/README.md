Implement a function which filters out array values which satisfy the given predicate.

```javascript
reject([1, 2, 3, 4, 5, 6], (n) => n % 2 === 0)  =>  [1, 3, 5]
```
```csharp
Kata.Reject(new int[] {1, 2, 3, 4, 5, 6}, (n) => n % 2 == 0)  =>  new int[] {1, 3, 5}
```
```php
reject([1, 2, 3, 4, 5, 6], function ($n) {return $n % 2 == 0;})  =>  [1, 3, 5]
```
```python
reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)  =>  [1, 3, 5]
```
```haskell
reject even [ 1, 2, 3, 4, 5, 6 ]  ->  [ 1, 3, 5 ]
```
```cpp
reject<int>({ 1, 2, 3, 4, 5, 6 }, [](int n) { return n % 2 == 0; })  => std::vector{ 1, 3, 5 }
```
```c
bool is_even(int x) { return x % 2 == 0; }
int array[6] = {1, 2, 3, 4, 5, 6};
size_t new_len = reject(6, array, is_even);
// new_len == 3; array == { 1, 3, 5 }
```