### Task
You've just moved into a perfectly straight street with exactly ```n``` identical houses on either side of the road. Naturally, you would like to find out the house number of the people on the other side of the street. The street looks something like this:


--------------------
### Street
```
1|   |6
3|   |4
5|   |2
```

Evens increase on the right; odds decrease on the left. House numbers start at ```1``` and increase without gaps.
When ```n = 3```, ```1``` is opposite ```6```, ```3``` opposite ```4```, and ```5``` opposite ```2```. 

-----------------
### Example
Given your house number ```address``` and length of street ```n```, give the house number on the opposite side of the street.

```javascript
overTheRoad(address, n)
overTheRoad(1, 3) = 6
overTheRoad(3, 3) = 4
overTheRoad(2, 3) = 5
overTheRoad(3, 5) = 8
```

```CoffeeScript
overTheRoad(address, n)
overTheRoad(1, 3) = 6
overTheRoad(3, 3) = 4
overTheRoad(2, 3) = 5
overTheRoad(3, 5) = 8
```

```TypeScript
overTheRoad(address, n)
overTheRoad(1, 3) = 6
overTheRoad(3, 3) = 4
overTheRoad(2, 3) = 5
overTheRoad(3, 5) = 8
```

```c
size_t over_the_road(size_t address, size_t n);
over_the_road(1, 3) == 6
over_the_road(3, 3) == 4
over_the_road(2, 3) == 5
over_the_road(3, 5) == 8
```

```crystal
over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8
```

```python
over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8
```

```julia
over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8
```

```ruby
over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8
```


```php
overTheRoad(address, n)
overTheRoad(1, 3) = 6
overTheRoad(3, 3) = 4
overTheRoad(2, 3) = 5
overTheRoad(3, 5) = 8
```

```prolog
over_the_road(Address, N, HouseNo)
over_the_road(1, 3, 6).
over_the_road(3, 3, 4).
over_the_road(2, 3, 5).
over_the_road(3, 5, 8).
```

```cfml
overTheRoad(address, n)
overTheRoad( 1, 3 ) = 6
overTheRoad( 3, 3 ) = 4
overTheRoad( 2, 3 ) = 5
overTheRoad( 3, 5 ) = 8
```

```java
CodeWars.overTheRoad(long address, long n)
CodeWars.overTheRoad(1, 3) = 6
CodeWars.overTheRoad(3, 3) = 4
CodeWars.overTheRoad(2, 3) = 5
CodeWars.overTheRoad(3, 5) = 8
```

```PowerShell
overTheRoad $address $n
overTheRoad 1 3 = 6
overTheRoad 3 3 = 4
overTheRoad 2 3 = 5
overTheRoad 3 5 = 8
```

```shell
over_the_road args: [ address, street ]
over_the_road: [ 1, 3 ] = 6
over_the_road: [ 3, 3 ] = 4
over_the_road: [ 2, 3 ] = 5
over_the_road: [ 3, 5 ] = 8
```

```dart
int overTheRoad(int address, int n)
overTheRoad(1, 3) = 6
overTheRoad(3, 3) = 4
overTheRoad(2, 3) = 5
overTheRoad(3, 5) = 8
```

```vb
OverTheRoad(ByVal address as Long, ByVal n as Long) as Long
OverTheRoad(1, 3) = 6
OverTheRoad(3, 3) = 4
OverTheRoad(2, 3) = 5
OverTheRoad(3, 5) = 8
```

```csharp
CodeWars.overTheRoad(long address, long n)
CodeWars.overTheRoad(1, 3) = 6
CodeWars.overTheRoad(3, 3) = 4
CodeWars.overTheRoad(2, 3) = 5
CodeWars.overTheRoad(3, 5) = 8
```

```cpp
over_the_road(long long address, long n);
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8
```
```rust
over_the_road(address: u64, n: u64) -> u64
over_the_road(1, 3) == 6
over_the_road(3, 3) == 4
over_the_road(2, 3) == 5
over_the_road(3, 5) == 8
```

## Note about errors
If you are timing out, running out of memory, or get any kind of "error", read on.
Both n and address could get upto 500 billion with over 200 random tests. If you try to store the addresses of 500 billion houses in a list then you will run out of memory and the tests will crash. This is not a kata problem so please don't post an issue. Similarly if the tests don't complete within 12 seconds then you also fail. 

To solve this, you need to think of a way to do the kata without making massive lists or huge for loops. Read the discourse for some inspiration :)


