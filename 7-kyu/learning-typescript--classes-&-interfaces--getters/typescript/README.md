# Learning TypeScript. Classes & Interfaces. Getters

N.B.: To solve this kata you need to choose "2.4/ES6" target.

## Task

Define the following classes:

### I. Cuboid

The object constructor for the class <code>Cuboid</code> should receive exactly three arguments in the following order: <code>length</code>, <code>width</code>, <code>height</code> and store these three values in <code>this.length</code>, <code>this.width</code> and <code>this.height</code> respectively.

The class <code>Cuboid</code> should then have a getter <code>surfaceArea</code> which returns the surface area of the cuboid and a getter <code>volume</code> which returns the volume of the cuboid.

### II. Cube

Class <code>Cube</code> is a subclass of class <code>Cuboid</code>. The constructor function of <code>Cube</code> should receive one argument only, its length, and use that value passed in to set <code>this.length</code>, <code>this.width</code> and <code>this.height</code>.

Hint: Make a call to <code>super</code>, passing in the correct arguments, to make life easier ;)

# Articles of Interest

Below are some articles of interest that may help you complete this Kata:
1. <a href="http://stackoverflow.com/questions/28222276/what-are-getters-and-setters-for-in-ecmascript-6-classes">Stack Overflow - What are getters and setters in ES6?</a>
2. <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get">getter - Javascript | MDN</a>

# Credits

This is TypeScript version of kata "<a href="http://www.codewars.com/kata/56fbdda707cff41b68000de2">Fun with ES6 Classes #3 - Cuboids, Cubes and Getters</a>" by @donaldsebleung


**P.S.** Solved this kata? Take a look at other katas in "<a href="https://www.codewars.com/collections/learning-typescript">Learning TypeScript</a>" collection.