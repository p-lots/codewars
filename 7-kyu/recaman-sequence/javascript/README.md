Return the `n`th term of the Recamán's sequence.

```
a(0) = 0;

        a(n-1) - n, if this value is positive and not yet in the sequence
      /
a(n) <
      \
        a(n-1) + n, otherwise
```

~~~if-not:lambdacalc,
input range: 0 – 30 000
~~~
~~~if:lambdacalc,
input range: 0 – 1 000

purity: `LetRec`  
numEncoding: `BinaryScott`  
~~~
___

Numberphile [video](https://www.youtube.com/watch?v=FGC5TdIiT9U) about Recamán's sequence
