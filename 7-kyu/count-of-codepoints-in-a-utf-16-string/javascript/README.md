[UTF-16](https://en.wikipedia.org/wiki/UTF-16) is a Unicode encoding. It is used by platforms and protocols such as the [Windows API](https://en.wikipedia.org/wiki/Windows_API), SMS texts, or the Qt GUI library.

It is also the internal encoding of strings in several programming languages: JavaScript, languages running on the [Java platform](https://en.wikipedia.org/wiki/Java_(software_platform)) (Java, Scala, Kotlin, Clojure...), languages running on the [.NET framework](https://en.wikipedia.org/wiki/.NET) (C#, F#, VB.NET, PowerShell...).
 
UTF-16 is a *variable-length* encoding: the representation of a *codepoint* can require either `1` or `2` 16-bit *code-units* , depending on whether the codepoint is below `$2^{16}$` or not.

## The problem

In languages that use UTF-16 as their string encoding, the function/method/property to retrieve the string's *length* actually returns the number of *code-units* in the string, not the number of *codepoints*.

## For example

The code point of the emoji `🙉` (`U+1F649`, *Hear-No-Evil Monkey*) is `0x1F649`.

```if:csharp,vb,fsharp,powershell
~~~csharp
"🙉".Length // 2
~~~
```
```javascript
'🙉'.length // 2
```
```java
"🙉".length() // 2
```
```c
sizeof u"🙉" // 6 bytes (note that it includes the nul terminator u'\0')
```
```cpp
std::u16string(u"🙉").length() // 2
```

## Task

Write a function that returns the number of codepoints in a UTF-16 string.

```
"abcd"     --> 4
"🙉"      --> 1
"😸🦌🚀" --> 3
"é"       --> 1 (actual é character)
"é"       --> 2 (e + combining acute accent)
```

## See also
[Same task](https://www.codewars.com/kata/68b8e7f8ce76e77dcfb77e8a) but in UTF-8, also a variable-length Unicode encoding.