# Description
You are required to implement a function `find_nth_occurrence` that returns the index of the nth occurrence of a substring within a string (considering that those substring could overlap each others). If there are less than n occurrences of the substring, return -1.

# Example
```python
string = "This is an example. Return the nth occurrence of example in this example string."
find_nth_occurrence("example", string, 1) == 11
find_nth_occurrence("example", string, 2) == 49
find_nth_occurrence("example", string, 3) == 65
find_nth_occurrence("example", string, 4) == -1
```
```c
const char *string = "This is an example. Return the nth occurrence of example in this example string.";
find_nth_occurrence("example", string, 1) == 11
find_nth_occurrence("example", string, 2) == 49
find_nth_occurrence("example", string, 3) == 65
find_nth_occurrence("example", string, 4) == -1
```
```java
String string = "This is an example. Return the nth occurrence of example in this example string.";
findNthOccurrence("example", string, 1) == 11
findNthOccurrence("example", string, 2) == 49
findNthOccurrence("example", string, 3) == 65
findNthOccurrence("example", string, 4) == -1
```

Multiple occurrences of a substring are allowed to overlap, e.g.
```python
find_nth_occurrence("TestTest", "TestTestTestTest", 1) == 0
find_nth_occurrence("TestTest", "TestTestTestTest", 2) == 4
find_nth_occurrence("TestTest", "TestTestTestTest", 3) == 8
find_nth_occurrence("TestTest", "TestTestTestTest", 4) == -1
```
```c
find_nth_occurrence("TestTest", "TestTestTestTest", 1) == 0
find_nth_occurrence("TestTest", "TestTestTestTest", 2) == 4
find_nth_occurrence("TestTest", "TestTestTestTest", 3) == 8
find_nth_occurrence("TestTest", "TestTestTestTest", 4) == -1
```
```java
findNthOccurrence("TestTest", "TestTestTestTest", 1) == 0
findNthOccurrence("TestTest", "TestTestTestTest", 2) == 4
findNthOccurrence("TestTest", "TestTestTestTest", 3) == 8
findNthOccurrence("TestTest", "TestTestTestTest", 4) == -1
```
