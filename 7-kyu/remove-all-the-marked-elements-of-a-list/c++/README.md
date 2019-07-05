Define a method/function that removes from a given array of integers all the values contained in a second array.

## Examples:
```python
l = List()

integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
values_list = [1, 3]
l.remove_(integer_list, values_list) == [2, 2, 4]

integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
lst = [1, 3, 4, 2]
l.remove_(integer_list, values_list) == [5, 6 ,7 ,8]

integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3]
lst = [2, 4, 3]
l.remove_(integer_list, values_list) == [8, 7, 6, 5, 1]
```
```csharp
int[] integerList = new int[]{ 1, 1, 2, 3, 1, 2, 3, 4 }
int[] valuesList = new int[]{ 1, 3 }
Kata.Remove(integerList, valuesList) == new int[]{ 2, 2, 4 } // --> true

int[] integerList = new int[]{ 1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8 }
int[] valuesList = new int[]{ 1, 3, 4, 2 }
Kata.Remove(integerList, valuesList) == new int[]{ 5, 6 ,7 ,8 } // --> true

int[] integerList = new int[]{ 8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3 }
int[] valuesList = new int[]{ 2, 4, 3 }
Kata.Remove(integerList, valuesList) == new int[]{ 8, 7, 6, 5, 1 } // --> true
```
Enjoy it!!

