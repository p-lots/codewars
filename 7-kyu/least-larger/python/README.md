### Task

Given an array of numbers and an index, return the index of the least number larger than the element at the given index, or `-1` if there is no such index ( or, where applicable, `Nothing` or a similarly empty value ).

### Notes

Multiple correct answers may be possible. In this case, return any one of them.  
The given index will be inside the given array.  
The given array will, therefore, never be empty.  

### Example

```javascript
leastLarger( [4, 1, 3, 5, 6], 0 )  =>  3
leastLarger( [4, 1, 3, 5, 6], 4 )  => -1
```
```haskell
leastLarger [4, 1, 3, 5, 6] 0  ->  Just 3
leastLarger [4, 1, 3, 5, 6] 4  -> Nothing
```
```c
least_larger({4, 1, 3, 5, 6}, 5, 0) ==  3;
least_larger({4, 1, 3, 5, 6}, 5, 4) == -1;
```
```python
least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1
```
```prolog
least_larger( [4, 1, 3, 5, 6], 0, 3 ).
least_larger( [4, 1, 3, 5, 6], 4, -1 ).
```
```ruby
least_larger( [4, 1, 3, 5, 6], 0 )  =  3
least_larger( [4, 1, 3, 5, 6], 4 )  = -1
```
```go
leastLarger( [] int {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( [] int {4, 1, 3, 5, 6}, 4 )  = -1
```
```java
leastLarger( new int [] {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( new int [] {4, 1, 3, 5, 6}, 4 )  = -1
```
```csharp
leastLarger( new int [] {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( new int [] {4, 1, 3, 5, 6}, 4 )  = -1
```
```cpp
leastLarger( vector<int> {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( vector<int> {4, 1, 3, 5, 6}, 4 )  = -1
```