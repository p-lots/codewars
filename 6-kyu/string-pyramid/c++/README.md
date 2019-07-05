You have to build a pyramid.<br>
<br>
This pyramid should be built from characters from a given string.<br>
<br>
You have to create the code for these four methods:
```csharp
public static string WatchPyramidFromTheSide(string characters)

public static string WatchPyramidFromAbove(string characters)

public static int CountVisibleCharactersOfThePyramid(string characters)

public static int CountAllCharactersOfThePyramid(string characters)
```
```java
public static String watchPyramidFromTheSide(String characters)

public static String watchPyramidFromAbove(String characters)

public static int countVisibleCharactersOfThePyramid(String characters)

public static int countAllCharactersOfThePyramid(String characters)
```
```javascript
function watchPyramidFromTheSide(characters)

function watchPyramidFromAbove(characters)

function countVisibleCharactersOfThePyramid(characters)

function countAllCharactersOfThePyramid(characters)
```
```cpp
std::string watchPyramidFromTheSide(std::string characters)

std::string watchPyramidFromAbove(std::string characters)

int countVisibleCharactersOfThePyramid(std::string characters)

int countAllCharactersOfThePyramid(std::string characters)
```
```python
watch_pyramid_from_the_side(characters):

watch_pyramid_from_above(characters):

count_visible_characters_of_the_pyramid(characters):

count_all_characters_of_the_pyramid(characters):
```

The first method ("FromTheSide") shows the pyramid as you would see from the side.<br>
The second method ("FromAbove") shows the pyramid as you would see from above.<br>
The third method ("CountVisibleCharacters") should return the count of all characters, that are visible from outside the pyramid.<br>
The forth method ("CountAllCharacters") should count all characters of the pyramid. Consider that the pyramid is completely solid and has no holes or rooms in it.<br>

Every character will be used for building one layer of the pyramid. So the length of the given string will be the height of the pyramid. Every layer will be built with stones from the given character. There is no limit of stones.<br>
The pyramid should have perfect angles of 45 degrees.<br>
<br><br>
Example: <b>Given string: "abc"</b><br>
<br>
Pyramid from the side:<br>
```
  c
 bbb
aaaaa
```
Pyramid from above:<br>
```
aaaaa
abbba
abcba
abbba
aaaaa
```
Count of visible stones/characters: 
```
25
```
Count of all used stones/characters:
```
35
```
<br>
There is no meaning in the order or the choice of the characters. It should work the same for example "aaaaa" or "54321".
<br>
<b>Hint:</b> Your output for the side must always be a rectangle! So spaces at the end of a line must not be deleted or trimmed!
<br>
If the string is null or empty, you should exactly return this value for the watch-methods and <b>-1</b> for the count-methods.
<br><br>
Have fun coding it and please don't forget to vote and rank this kata! :-) <br>

I have created other katas. Have a look if you like coding and challenges.<br>