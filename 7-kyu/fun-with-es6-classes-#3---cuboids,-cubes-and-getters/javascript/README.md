# Fun with ES6 Classes #3 - Cuboids, Cubes and Getters

## Task

Define the following classes.

### I. Cuboid

The object ```constructor``` for the ```class Cuboid``` should receive exactly three arguments in the following order: ```length, width, height``` and store these three values in ```this.length```, ```this.width``` and ```this.height``` respectively.

The ```class Cuboid``` should then have a **getter** ```surfaceArea``` which returns the surface area of the cuboid and a getter ```volume``` which returns the volume of the cuboid.

### II. Cube

```class Cube``` is a subclass of ```class Cuboid```.  The ```constructor``` function of ```Cube``` should receive one argument only, its ```length```, and use that value passed in to set ```this.length```, ```this.width``` and ```this.height```.

*Hint: Make a call to ```super```, passing in the correct arguments, to make life easier ;)*

## Related Articles

Listed below are a few articles of interest that may help you complete this Kata:

1. [Stack Overflow - What are getters and setters in ES6?](http://stackoverflow.com/questions/28222276/what-are-getters-and-setters-for-in-ecmascript-6-classes)
2. [getter - Javascript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)