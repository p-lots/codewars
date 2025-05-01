```if:csharp
In C# 6.0 there is new operator `?.` called the **Null-Conditional Operator**.
```
```if:javascript
In ECMAScript 2020, there is a new operator `?.` called the **optional chaining operator**. This operator is available from Node.js v14 onwards.
```

It's nothing revolutionary - just an example of syntactic sugar but a pretty neat one.

## Use case

Imagine you have a `Car`, the car has an `Engine`, the engine has a `Gearbox` and the gearbox has some property you are interested in, for example `numberOfGears`. Now, the car could be from junkyard and the gearbox or even the engine could be missing (`null`).

The name of each property is the name of the class it contains, converted to the appropriate case, such that if all components are present the final property could be accessed by:

```if:csharp
`Car.Engine.GearBox.NumberOfGears`
```
```if:javascript
`Car.engine.gearbox.numberOfGears`
```

**How to determine the number of gears in a car?**

## Instructions

```if:csharp
Write an extension method for `Car` called `GetNumberOfGears`. This method will return the value of `NumberOfGears` property of the gearbox or `-1` if the gearbox (or anything else) is missing.
```
```if:javascript
Complete the method called `getNumberOfGears` being added to the prototype of the `Car` class. This method will return the value of the `numberOfGears` property of the gearbox or `null` if the gearbox (or anything else) is missing.
```

### Constraints

Find some information about the `?.` and `??` operators and try to write the method without using `if` or the ternary operator `?:`.

```if:csharp
## References

* [Null-conditional Operators (?.)](https://msdn.microsoft.com/en-us/library/dn986595.aspx)
* [Null-coalescing operator (??)](https://msdn.microsoft.com/en-us/library/ms173224.aspx)
* [Conditional operator (?:)](https://msdn.microsoft.com/en-us/library/ty67wk28%28v=vs.120%29.aspx)
```


