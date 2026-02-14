Write a function that, given a column title as it appears in an Excel sheet, returns its corresponding column number. 

All column titles will be uppercase.

Examples:
```
Column title: "A" --> return 1
Column title: "Z" --> return 26
Column title: "AA" --> return 27
```


```if:clojure
Note for Clojure:
Don't use Java Math/pow (even with bigint) because there is a loss of precision 
when the length of "title" is growing. 
Write your own function "exp [x n]".
```


