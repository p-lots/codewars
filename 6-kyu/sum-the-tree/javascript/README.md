Given a node object representing a binary tree:

```javascript
// example of a node object:
const node = {
   value: 1,
   left: {value: 2, right: null, left: null},
   right: null
};
```

```c
struct node
{
    int value;
    struct node* left;
    struct node* right;
};
```

```cpp
struct node
{
  int value;
  node* left;
  node* right;
}
```

```csharp
public class Node
{  
    public int Value;  
    public Node Left;  
    public Node Right;
    
    public Node(int value, Node left = null, Node right = null)
    {
      Value = value;
      Left = left;
      Right = right;
    }
}  
```

```rust
#[derive(Debug)]
struct Node {
    pub value: i32,
    pub left: Option<Box<Node>>,
    pub right: Option<Box<Node>>,
}
```



write a function that returns the sum of all values, including the root. Absence of a node will be indicated with a `null` value.

Examples:
```
10
| \
1  2
=> 13

1
| \
0  0
    \
     2
=> 3
```