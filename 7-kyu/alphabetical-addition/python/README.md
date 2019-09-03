Your task is to add up letters to one letter.
```if-not:haskell,crystal,cpp,dart,elixir,reason,c
The function will be given a variable amount of arguments, each one being a letter to add.
```
```if:crystal,reason
The function will be given an array of letters, each one being a letter to add.
```
```if:haskell,dart,elixir
The function will be given a list of letters, each one being a letter to add.
```
```if:cpp
The function will be given a vector of letters, each one being a letter (of type char) to add.

Return type char too.
```
```if:c
The function will be given the array size, and an array of characters, each one being a letter to add.
```
## Notes:
* Letters will always be lowercase.
* Letters can overflow (see second to last example of the description)
* No letters should return 'z'

## Examples:
```javascript
addLetters('a', 'b', 'c') = 'f'
addLetters('a', 'b') = 'c'
addLetters('z') = 'z'
addLetters('z', 'a') = 'a'
addLetters('y', 'c', 'b') = 'd' // notice the letters overflowing
addLetters() = 'z'
```
```php
addLetters('a', 'b', 'c') = 'f'
addLetters('a', 'b') = 'c'
addLetters('z') = 'z'
addLetters('z', 'a') = 'a'
addLetters('y', 'c', 'b') = 'd' // notice the letters overflowing
addLetters() = 'z'
```
```typescript
addLetters('a', 'b', 'c') = 'f'
addLetters('a', 'b') = 'c'
addLetters('z') = 'z'
addLetters('z', 'a') = 'a'
addLetters('y', 'c', 'b') = 'd' // notice the letters overflowing
addLetters() = 'z'
```
```coffeescript
addLetters('a', 'b', 'c') = 'f'
addLetters('a', 'b') = 'c'
addLetters('z') = 'z'
addLetters('z', 'a') = 'a'
addLetters('y', 'c', 'b') = 'd' # notice the letters overflowing
addLetters() = 'z'
```
```ruby
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'
```
```python
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'
```
```cpp
add_letters({'a', 'b', 'c'}) = 'f'
add_letters({'a', 'b'}) = 'c'
add_letters({'z'}) = 'z'
add_letters({'z', 'a'}) = 'a'
add_letters({'y', 'c', 'b'}) = 'd' # notice the letters overflowing
add_letters({}) = 'z'
```
```crystal
add_letters(['a', 'b', 'c']) = 'f'
add_letters(['a', 'b']) = 'c'
add_letters(['z']) = 'z'
add_letters(['z', 'a']) = 'a' # note single quotes, we work with Chars
add_letters(['y', 'c', 'b']) = 'd' # notice the letters overflowing
add_letters([] of Char) = 'z'
```
```elixir
add_letters(["a", "b", "c"]) = "f"
add_letters(["a", "b"]) = "c"
add_letters(["z"]) = "z"
add_letters(["z", "a"]) = "a"
add_letters(["y", "c", "b"]) = "d" # notice the letters overflowing
add_letters([]) = "z"
```
```dart
addLetters(['a', 'b', 'c']) = 'f'
addLetters(['a', 'b']) = 'c'
addLetters(['z']) = 'z'
addLetters(['z', 'a']) = 'a'
addLetters(['y', 'c', 'b']) = 'd' // notice the letters overflowing
addLetters(<String>[]) = 'z'
```
```reason
addLetters([|"a", "b", "c"|]) = "f"
addLetters([|"a", "b"|]) = "c"
addLetters([|"z"|]) = "z"
addLetters([|"z", "a"|]) = "a"
addLetters([|"y", "c", "b"|]) = "d" /* notice the letters overflowing */
addLetters([||]) = "z"
```
```julia
addletters('a', 'b', 'c') = 'f'
addletters('a', 'b') = 'c'
addletters('z') = 'z'
addletters('z', 'a') = 'a' # note single quotes, we work with Chars
addletters('y', 'c', 'b') = 'd' # notice the letters overflowing
addletters() = 'z'
```
```haskell
addLetters ['a', 'b', 'c'] = 'f'
addLetters ['a', 'b'] = 'c'
addLetters ['z'] = 'z'
addLetters ['z', 'a'] = 'a'
addLetters ['y', 'c', 'b'] = 'd' -- notice the letters overflowing
addLetters [] = 'z'
```
```c
add_letters(3, {'a', 'b', 'c'}) == 'f'
add_letters(2, {'a', 'b'})      == 'c'
add_letters(1, {'z'})           == 'z'
add_letters(2, {'z', 'a'})      == 'a'
add_letters(3, {'y', 'c', 'b'}) == 'd' // notice letters overflowing
add_letters(0, {})              == 'z'
```