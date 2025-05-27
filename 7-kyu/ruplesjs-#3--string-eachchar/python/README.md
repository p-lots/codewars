Your team is really excited with all the contributions you've made to the RuplesJS library. They feel the work you're doing will truly help Ruby developers transition to Javascript! They've assigned you another task.

## String.eachChar()

In ruby you can add something after each character in a string like so:
````
"hello".each_char {|c| print c, ' ' } -> "h e l l o " 
````

In the spirit of polymorphism, our eachChar method will allow one of two arguments, a callback function or a string. If a string is presented, it will be added after each character of the original string and return the new string. If a function is presented, it will perform a manipulation of each character in the string.

Example:

```javascript
"hello".eachChar(" ");
-> "h e l l o "

"hello all".eachChar(function(char) {
  if (char == "l") {
    return char.toUpperCase();
  } else {
    return char;
  }
});
-> "heLLo aLL"
```
```python
each_char("hello"," ")
-> "h e l l o "

def func(c):
    return 'L' if c=='l' else c
    
each_char("hello all", func)
-> "heLLo aLL"
```
```ruby
"hello".each_char(" ")
-> "h e l l o "

def func(c)
    return c=='l' ? 'L' : c
end
"hello all".each_char(:func)
-> "heLLo aLL"
```

Please add your contribution to RuplesJS!

<div style="width: 320px; text-align: center; color: white; border: white 1px solid;">
Check out my other RuplesJS katas:
</div>
<div>
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-1-n-times-do'><span style='color:#00C5CD'>RuplesJS #1:</span> N Times Do</a><br />
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-2-string-delete'><span style='color:#00C5CD'>RuplesJS #2:</span> String Delete</a><br />
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-3-string-eachchar'><span style='color:#00C5CD'>RuplesJS #3:</span> String EachChar</a><br />
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-4-string-formatting'><span style='color:#00C5CD'>RuplesJS #4:</span> String Formatting</a><br />
<a style='text-decoration:none' href='http://www.codewars.com/kata/ruplesjs-number-5-range'><span style='color:#00C5CD'>RuplesJS #5:</span> Range</a><br />
</div>