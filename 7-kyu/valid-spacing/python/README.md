## Task
Your task is to write a function called ```valid_spacing()``` or ```validSpacing()```  which checks if a string has valid spacing. The function should return either ```True``` or ```False```.  

For this kata, the definition of valid spacing is one space between words, and no leading or trailing spaces. Below are some examples of what the function should return.
```php
'Hello world' = true
' Hello world' = false
'Hello world  ' = false
'Hello  world' = false
'Hello' = true
// Even though there are no spaces, it is still valid because none are needed
'Helloworld' = true 
// true because we are not checking for the validity of words.
'Helloworld ' = false
' ' = false
'' = true
```
```c
valid_spacing("Hello world");   return true
valid_spacing(" Hello world");  return false
valid_spacing("Hello world  "); return false
valid_spacing("Hello  world");  return false
valid_spacing("Hello");         return true
// Even though there are no spaces, it is still valid because none are needed.
valid_spacing("Helloworld");    return true
// True because we are not checking for the validity of words.
valid_spacing("Helloworld ");   return false
valid_spacing(" ");             return false
valid_spacing("");              return true
```

```javascript
'Hello world' = true
' Hello world' = false
'Hello world  ' = false
'Hello  world' = false
'Hello' = true
// Even though there are no spaces, it is still valid because none are needed
'Helloworld' = true 
// true because we are not checking for the validity of words.
'Helloworld ' = false
' ' = false
'' = true
```

```python
'Hello world' = True
' Hello world' = False
'Hello world  ' = False
'Hello  world' = False
'Hello' = True
# Even though there are no spaces, it is still valid because none are needed
'Helloworld' = True 
# True because we are not checking for the validity of words.
'Helloworld ' = False
' ' = False
'' = True
```
*Note - there will be no punctuation or digits in the input string, only letters.*

