# Learning TypeScript. Classes & Interfaces. Setters

N.B.: To solve this kata you need to choose "2.4/ES6" target.

## Overview

In "<a href="https://www.codewars.com/kata/learning-typescript-classes-and-interfaces-getters">Learning TypeScript. Classes & Interfaces. Getters</a>", we learned that if we knew all the dimensions (i.e. <code>length</code>, <code>width</code>, <code>height</code>) of a cuboid, we could easily work out its corresponding volume and surface area. The way we achieved this in our code was by the use of getters which automatically computed the volume and surface area of the cuboid whenever either one of length, width, height changed. However, in the previouos exercise, one thing we could not do is define setters for surface area or volume of a cuboid because for a given volume/SA, there were an infinite number of possibilities to the dimensions of the cuboid.

However, for cubes (a special type of cuboid), since their length, width and height are always the same, it is possible to figure out the side length of a cube given its surface area and/or volume. Therefore, in this Kata, you will be asked to define setters as well as getters for both the surface area and volume of a cube.

## Task

You're given the <code>ICuboid</code> interface. Define a class <code>Cube</code> that implements <code>ICuboid</code>. Constructor function of <code>Cube</code> takes exactly one parameter <code>length</code> and stores the value of the argument into <code>this.length</code>. You will then define both a getter and a setter for the <code>surfaceArea</code> and <code>volume</code> of the cube.

# Articles of Interest

Below are some articles of interest that may help you complete this Kata:

1. <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set">Setters - Mozilla Developer</a>
2. <a href="http://stackoverflow.com/questions/28222276/what-are-getters-and-setters-for-in-ecmascript-6-classes">What are getters and setters? - Stack Overflow</a>
3. <a href="http://exploringjs.com/es6/ch_classes.html">ES6 Classes Intro (includes section on getters and setters)</a>

# Credits

This is TypeScript version of kata "<a href="https://www.codewars.com/kata/fun-with-es6-classes-number-4-cubes-and-setters/javascript">Fun with ES6 Classes #4 - Cubes and Setters</a>" by @donaldsebleung


**P.S.** Solved this kata? Take a look at other katas in "<a href="https://www.codewars.com/collections/learning-typescript">Learning TypeScript</a>" collection.
