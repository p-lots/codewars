Do you remember the old mobile display keyboards? Do you also remember how inconvenient it was to write on it?  
Well, here you have to calculate how much keystrokes you have to do for a specific word.

This is the layout:

<img src="https://raw.githubusercontent.com/zruF/CodewarsData/master/Mobile_phone_keyboard.svg.png" style="max-width:20%;max-height:20%"/>

Return the amount of keystrokes of input `str` (! only letters, digits and special characters in lowercase included in layout without whitespaces !)

### Examples

```
mobileKeyboard("*#") => 2 (1+1)
mobileKeyboard("123") => 3 (1+1+1)
mobileKeyboard("abc") => 9 (2+3+4)
mobileKeyboard("codewars") => 26 (4+4+2+3+2+2+4+5)
```