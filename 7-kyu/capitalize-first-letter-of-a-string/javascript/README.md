# Capitalize First Letter of a String

Write a function `capitalize()` which capitalizes the first letter (if any) of the given string.  For example:

| Input | Output |
| --- | --- |
| `string` | `String` |
| `hello World` | `Hello World` |
| `i love codewars` | `I love codewars` |
| `This sentence is already capitalized` | `This sentence is already capitalized` |
| `0123the first character of this sentence is not a letter` | `0123the first character of this sentence is not a letter` |

~~~if:javascript,coffeescript
JavaScript / CoffeeScript: Extend the `String` prototype with a method `capitalize()` so you can call it on a string like so: `"string".capitalize()`. Learn about [inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain).

Furthermore, the built-in string methods `toUpperCase()` and `toLowerCase()` are disabled for this Kata.
~~~

~~~if:riscv
RISC-V: The function signature is

```c
void capitalize(const char *str, char *out);
```

`str` is the input string. You should write the capitalized result to `out`. You may assume `out` is large enough to hold the result. You do not need to return anything.

Your solution should handle `NULL` input gracefully by returning immediately.
~~~