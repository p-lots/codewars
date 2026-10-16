Consider the string `"adfa"` and the following rules: 

1. Each character MUST be changed either to the one before or the one after in alphabet. 
1. Characters `a` can only be changed to `b` and `z` to `y`. 

For some example strings, we get:

```
"adfa" -> ["begb","beeb","bcgb","bceb"]
"bd" -> ["ae","ac","ce","cc"]
```

We see that in each example, one of the outcomes is a palindrome. That is, `"beeb"` and `"cc"`.

You will be given a lowercase string and your task is to return `True` if at least one of the outcomes is a palindrome or `False` otherwise. 

More examples in test cases. Good luck!
