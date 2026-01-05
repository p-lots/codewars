#### Task:

Build a string representing a capital letter C of a given size out of 'C' characters.

#### Examples: 

```python,lua
generate_C(1) 
```
```java
generateC(1) 
```
```csharp
GenerateC(1)
```
should return this string:
```
CCCCC
C
C
C
CCCCC
```

```python,lua
generate_C(2) 
```
```java
generateC(2)
```
```csharp
GenerateC(2)
```
should be
```
CCCCCCCCCC
CCCCCCCCCC
CC
CC
CC
CC
CC
CC
CCCCCCCCCC
CCCCCCCCCC
```

and so on. Given <code>size</code>, the string should have <code>5*size</code> lines, following the format above.  <code>size</code> is a positive integer <code>&le; 2000.</code>

Note that extra spaces after the C's in any line are incorrect. And the last line should not terminate with "\n".

This kata was inspired by [A for Apple](https://www.codewars.com/kata/55de3f83e92c3e521a00002a), but takes a different approach to generating letters.