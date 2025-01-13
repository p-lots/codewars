Given a string, you progressively need to concatenate the first character from the left and the first character from the right and "1", then the second character from the left and the second character from the right and "2", and so on.

If the string's length is odd drop the central element.

For example:
```python
char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
```
```javascript
charConcat("abcdef")    == 'af1be2cd3'
charConcat("abc!def")   == 'af1be2cd3' // same result
```
```ruby
char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
```
