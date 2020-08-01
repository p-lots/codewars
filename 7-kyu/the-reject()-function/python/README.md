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