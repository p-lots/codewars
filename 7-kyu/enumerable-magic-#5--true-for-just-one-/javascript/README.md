## Task

Create a function called `one` that accepts two params:

* a sequence 
* a function

and returns `true` only if the function in the params returns `true` for exactly one (`1`) item in the sequence. 

## Example

```
one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten) -> true
one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) -> false
one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten) -> false
```

~~~if:ruby
If you need help, [here](https://docs.ruby-lang.org/en/master/Enumerable.html#method-i-one-3F) is a resource (in Ruby).
~~~
~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `Church`  
export constructors `nil, cons` for your `List` encoding  
export constructors `False, True` and deconstructors `if` for your `Bool` encoding
~~~
