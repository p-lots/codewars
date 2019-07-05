## Sum and Length

In this kata you must return a string value, where the first part is the sum of positive numbers and the second part is the number of negative numbers.<br><b>Knowing</b> that the first '0' is negative, the second is positive etc...

<b><h3>For example :</h3></b>

```javascript
sumLength([-1,2,3,4,0,1,0,-2,0,-3])
return '10 5' (10 = 1 + 2 + 3 + 4 and 5 = 3 + 2 => 3 negatives numbers + second 0 as negative)
```
```csharp
SumLength(new[] {-1, 2, 3, 4, 0, 1, 0, -2, 0, -3})
return "10 5" (10 = 1 + 2 + 3 + 4 and 5 = 3 + 2 => 3 negatives numbers + second 0 as negative)
```
```cpp
sumLength(std::vector<int> { -1, 2, 3, 4, 0, 1, 0, -2, 0, -3 });
return "10 5" (10 = 1 + 2 + 3 + 4 and 5 = 3 + 2 => 3 negatives numbers + second 0 as negative)
```

```php
sum_length([-1, 2, 3, 4, 0, 1, 0, -2, 0, -3]); // returns "10 5" (10 = 1 + 2 + 3 + 4 and 5 = 3 + 2 => 3 negatives numbers + second 0 as negative)
```