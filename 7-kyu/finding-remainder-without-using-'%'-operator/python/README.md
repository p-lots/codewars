## Task

Write a method `remainder` which takes two integer arguments, `dividend` and `divisor`, and returns the remainder when dividend is divided by divisor. Do <b>NOT</b> use the modulus operator (%) to calculate the remainder!

#### Assumption

Dividend will always be `greater than or equal to` divisor.

#### Notes

Make sure that the implemented `remainder` function works exactly the same as the `Modulus operator (%)`.

```if:c
Note for C: `div()`, `fmod()`, `ldiv()`, `lldiv()`, `fmodf()`, and `fmodl()` have all been disabled.
```

```if:java
`SimpleInteger` is a tiny and immutable implementation of an integer number. Its interface is a very small subset of the `java.math.BigInteger` API:

* `#add(SimpleInteger val)`
* `#subtract(SimpleInteger val)`
* `#multiply(SimpleInteger val)`
* `#divide(SimpleInteger val)`
* `#compareTo(SimpleInteger val)`
```
~~~if:python
`divmod` has also been disabled.
~~~