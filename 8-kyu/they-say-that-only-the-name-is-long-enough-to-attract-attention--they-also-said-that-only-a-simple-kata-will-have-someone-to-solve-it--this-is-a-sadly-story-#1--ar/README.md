<p align="center"><font size=5><b>They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it series #1:<br>Are they opposite?<br><font size=3></b></font></p>

# #Task
Give you two strings: ```s1``` and ```s2```. If they are opposite, return `true`; otherwise, return `false`. Note: The result should be a boolean value, instead of a string.

The ```opposite``` means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string.  Also take note of the edge case - if both strings are empty then you should return `false`/`False`.
  
# #Some examples:

```javascript
isOpposite("ab","AB") should return true;
isOpposite("aB","Ab") should return true;
isOpposite("aBcd","AbCD") should return true;
isOpposite("AB","Ab") should return false;
isOpposite("","") should return false;
```
```purescript
isOpposite "ab" "AB" -- => true
isOpposite "aB" "Ab" -- => true
isOpposite "aBcd" "AbCD" -- => true
isOpposite "AB" "Ab" -- => false
isOpposite "" "" -- => false
```
   
<div align="left" style="margin:0 auto;"><div style="width:1200px;height:800px;overflow:hidden;border:0px"><div style="width:500px;height:800px;margin:-393px -5000px 0px 0px;"><iFrame src="https://www.codewars.com/kata/57b55863d2a31c57720011c6" width="400" height="1000" scrolling="no" frameborder="0"></iFrame></div></div></div>