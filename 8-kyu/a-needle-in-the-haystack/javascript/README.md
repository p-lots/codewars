Can you find the needle in the haystack?

Write a function `findNeedle()` that takes an `array` full of junk but containing one `"needle"`

After your function finds the needle it should return a message (as a string) that says:

`"found the needle at position "` plus the `index` it found the needle, so: 

```python
find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```
```ruby
find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```
```elixir
find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```
```javascript
findNeedle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```
```typescript
findNeedle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```
```java
findNeedle(new Object[] {"hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"})
```
```haskell
findNeedle ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
```
```racket
(find-needle '("hay" "junk" "hay" "hay" "moreJunk" "needle","randomJunk"))
```
```cobol
      FindNeedle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```

should return `"found the needle at position 5"` (in COBOL `"found the needle at position 6"`)