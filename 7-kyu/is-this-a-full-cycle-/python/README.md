# Task
Imagine you have a list of integers. You start at the first item and use each value as a guide to decide where to go next.

Create a function that determines whether the input list forms a complete cycle or not.

![image](https://i.imgur.com/TRu0Bzk.png)

# Examples
```
[1, 4, 3, 0, 2] ➞ True

# When you follow the list [1, 4, 3, 0, 2] as shown in the image,
# you visit every item once and return to the starting point, making it a "full cycle."

[1, 4, 0, 3, 2] ➞ False

[5, 3, 4, 2, 0, 1] ➞ True
```

# Notes
- The list will not contain any duplicate values.
- All values are less than the length of the list (i.e., they are valid indices).
- 2 <= len(lst) <= 100