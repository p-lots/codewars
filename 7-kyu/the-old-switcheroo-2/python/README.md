This is a follow up from my kata <a href='http://www.codewars.com/kata/55d410c492e6ed767000004f'>The old switcheroo</a>



Write the function :
```javascript
function encode(str)
```
```python
def encode(str)
```
```ruby
def encode(str)
```
```coffeescript
encode = (str) ->
```
```csharp
public static string Encode(string str)
```
that takes in a string ```str``` and replaces all the letters with their respective positions in the English alphabet.<br/>

```javascript
encode('abc') == '123'   // a is 1st in English alpabet, b is 2nd and c is 3rd
encode('codewars') == '315452311819'
encode('abc-#@5') == '123-#@5'
```
```python
encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
encode('codewars') == '315452311819'
encode('abc-#@5') == '123-#@5'
```
```ruby
encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
encode('codewars') == '315452311819'
encode('abc-#@5') == '123-#@5'
```
```coffeescript
encode 'abc' == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
encode 'codewars' == '315452311819'
encode 'abc-#@5' == '123-#@5'
```
```csharp
Encode("abc") == "123" // a is 1st in English alpabet, b is 2nd and c is 3rd
Encode("codewars") == "315452311819"
Encode("abc-#@5") == "123-#@5"
```
String are case sensitive.
```javascript
// Bonus point if you don't use toLowerCase()
```
```coffeescript
# Bonus point if you don't use toLowerCase()
```
```csharp
// Bonus point if you don't use ToLower()
```

