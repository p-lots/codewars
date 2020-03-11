The main mode is having a method named `main` inside a class and should return nothing but should print a line to the standard output with the message `Hello World!` i.e. print the line Hello World! to the console.
For Java the main method should receive `String` array as parameters that can be specified when running from console with the command.
In many traditional programming languages can be only one main for a whole application since it denotes the application entry point.

```java
    java Solution.class parameter1 parameter2
```    

```javascript
    Solution.main("parameter1","parameter2");
```  

```coffeescript
    Solution.main "parameter1", "parameter2","parametern"
```

```ruby
    Solution.main("parameter1", "parameter2","parametern")
```

```python
    Solution.main("parameter1", "parameter2","parametern")
    
    *Note:* please be sure to define main as static method
```

```csharp
   Solution.Main("parameter1", "parameter2","parametern")
```

```php
   Solution::main("parameter1", "parameter2", "parametern")
```
```sh
   no extra lines there
```

```prolog
   greet:greet
```

Hints:

 1. Check your references 
 2. Think about the scope of your method
 3. For prolog you can use write but there are [better ways](https://gist.github.com/dtonhofer/20bd01f68a924912771d8405fca66a09)