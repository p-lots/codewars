You've been collecting change all day, and it's starting to pile up in your pocket, but you're too lazy to see how much you've found.

Good thing you can code!

Complete the function to return a dollar amount of how much change you have!

Valid types of change include:
```
penny: 0.01
nickel: 0.05
dime: 0.10
quarter: 0.25
dollar: 1.00
```

```if:python
These amounts are already preloaded as floats into the `CHANGE` dictionary for you to use!
```
```if:ruby
These amounts are already preloaded as floats into the `CHANGE` hash for you to use!
```
```if:javascript
These amounts are already preloaded as floats into the `CHANGE` object for you to use!
```
```if:php
These amounts are already preloaded as floats into the `CHANGE` (a constant) associative array for you to use!
```

You should return the total in the format ```$x.xx```.

Examples:

```python
"nickel penny dime dollar" --> "$1.16"
"dollar dollar quarter dime dime" --> "$2.45"
"penny" --> "$0.01"
"dime" --> "$0.10"
```

Warning, some change may amount to over ```$10.00```!