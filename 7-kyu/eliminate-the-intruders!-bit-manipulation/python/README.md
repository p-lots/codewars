# Task

You are given a string representing a number in binary. Your task is to delete all the **unset** bits in this string and return the corresponding number (after keeping only the '1's). 

In practice, you should implement this function:

~~~if:nasm
```c
unsigned long eliminate_unset_bits(const char* number);
```
~~~
~~~if-not:nasm
```c
long eliminate_unset_bits(const char* number);
```
```python
def eliminate_unset_bits(number):
```
```javascript
function eliminateUnsetBits(number);
```
```ruby
def eliminate_set_bits number
```
```java
public long eliminateUnsetBits(String number);
```
```cpp
long eliminate_unset_bits(string number);
```
~~~

## Examples

~~~if:java,ruby,javascript
```java
eliminateUnsetBits("11010101010101") ->  255 (= 11111111)
eliminateUnsetBits("111") ->  7
eliminateUnsetBits("1000000") -> 1
eliminateUnsetBits("000") -> 0
```
```ruby
eliminate_set_bits("11010101010101") ->  255 (= 11111111)
eliminate_set_bits("111") ->  7
eliminate_set_bits("1000000") -> 1
eliminate_set_bits("000") -> 0
```
```javascript
eliminateUnsetBits("11010101010101") ->  255 (= 11111111)
eliminateUnsetBits("111") ->  7
eliminateUnsetBits("1000000") -> 1
eliminateUnsetBits("000") -> 0
```
~~~
~~~if-not:java,ruby,javascript
```c
eliminate_unset_bits("11010101010101") ->  255 (= 11111111)
eliminate_unset_bits("111") ->  7
eliminate_unset_bits("1000000") -> 1
eliminate_unset_bits("000") -> 0
```
~~~
