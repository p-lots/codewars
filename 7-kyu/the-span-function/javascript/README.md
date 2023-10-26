The span function is a good one to know. It accepts a sequence and a predicate function and returns two sequences. The first sequence contains all the elements of the argument sequence up to the item that caused the first failure of the predicate. The second returned sequence contains the rest of the original sequence. The original sequence is not modified.

For example,

```javascript

function isEven (x) {
  return Math.abs(x) % 2 === 0;
}

var arr = [2,4,6,1,8,10];

// This is true
span(arr, isEven) === [[2,4,6],[1,8,10]]
```
```ocaml
let is_even n = n mod 2 = 0 in
span [2; 4; 6; 8; 1; 2; 5; 4; 3; 2] is_even
  (* -> ( [2; 4; 6; 8], [1; 2; 5; 4; 3; 2] ) *)
```

Your task is to...wait for it... write your own span function !!!

Hint/Challenge: If you have completed [the takeWhile function](http://www.codewars.com/kata/the-takewhile-function) and [the dropWhile function](http://www.codewars.com/kata/the-dropwhile-function), then you can solve this problem in one line!