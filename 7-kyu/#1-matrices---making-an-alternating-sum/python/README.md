We have a matrix of integers with m rows and n columns.


```math
\begin{pmatrix}
   a_{11} & a_{12} & \cdots &a_{1n} \\
   a_{21} & a_{22}  &\cdots &a_{2n} \\
   \cdots & \cdots & \cdots & \cdots \\
   \cdots & \cdots & \cdots & \cdots \\
    a_{m1} & a_{m2} & \cdots &a_{mn}
\end{pmatrix}
```

We want to calculate the total sum for the matrix:


```math
\displaystyle\sum_{i=1}^{m} \sum_{j=1}^{n} (-1)^{i+j}a_{ij}
```

As you can see, the name "alternating sum" of the title is due to the sign of the terms that changes from one term to its contiguous one and so on.

Let's see an example:
```
matrix = [[1, 2, 3], [-3, -2, 1], [3, - 1, 2]]

total_sum = (1 - 2 + 3) + [-(-3) + (-2) - 1] + [3 - (-1) + 2] = 2 + 0 + 6 = 8
```
You may be given matrixes with their dimensions between these values:```10 < m < 300``` and ```10 < n < 300```.

More example cases in the Example Test Cases.
Enjoy it!!
