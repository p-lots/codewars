We have learned four basic array methods, ```pop()```, ```push()```, ```shift()``` and ```unshift()```, they are used to add or remove an array of elements. But their disadvantage is that they can only add or remove elements in order. This time we learn a new method: ```splice()```. It can add and/or remove elements at any location in the array. Its usage:
```
arrayObject.splice(startindex, deleteCount [,element1, element1, ...,elementx])
```
parameter1 and parameter2 are used to remove element. parameters in the ```[]``` is some elements to add, if we omitted it, ```splice()``` only performs removal operations.

We can write that way:
```
arrayObject.splice(a,b,[c,d,e,...,z])
```
Then ask yourself three questions:
```
Where do I start removing elements?   ---- a
How many elements need to be removed? ---- b
What elements should be added after the removal of the element?
--- c,d,e,...z
```
Some examples to help you understand ```splice()```
```javascript
function removeOdd(arr){
  //remove odd number of arr
  for (var i=arr.length;i>=0;i--)
    if (arr[i]%2) arr.splice(i,1)
  return arr;
}
console.log(removeOdd([1,2,3,4,5]))   //output: [ 2, 4 ]
console.log(removeOdd([1,3,5,7,9]))   //output: []
```
The example above removes all the odd numbers from the array, leaving all the even numbers. 

Why don't I start to traverse the array from index0? because we 
need to pay special attention to that some of the methods of the array ```directly modify the original array```. In some cases, if you forget the fact, you will get the wrong result. In the example above, if we start to traverse the array from index0, some element will be missed:
```javascript
function removeOdd(arr){
  //remove odd number of arr
  for (var i=0;i<arr.length;i++)
    if (arr[i]%2) arr.splice(i,1)
  return arr;
}
console.log(removeOdd([1,3,5,7,9]))   //output: [3,7]
because:
When i=0, arr[i]=1, arr.splice(0,1) then arr=[3,5,7,9], i++
then i=1, arr[i]=5, element 3 is missed because its index is became to 0
so, we got an wrong answer...
```
Look at the following example:
```javascript
function removeOdd(arr){
  //remove odd number from arr
  for (var i=arr.length;i>=0;i--)
    if (arr[i]%2) arr.splice(i,1)
  return arr;
}
function removeEven(arr){
  //remove even number from arr
  for (var i=arr.length;i>=0;i--)
    if (arr[i]%2==0) arr.splice(i,1)
  return arr;
}
var arr=[1,2,3,4,5]
removeOdd(arr)
console.log(arr)   //output: [ 2, 4 ]
removeEven(arr)
console.log(arr)   //output: []
```
Perhaps the purpose of running removeEven is to remove the even number, leaving the odd number. But in fact, we get an empty array, which is not what we want. How to improve it?

In this case, you can use ```slice()``` to make a "copy" for the array. In the previous study of string objects, We have known the slice, which is used to intercept a string. For an array object, the usage of ```slice()``` is similar to the stringObject method. Some people may want to use ```"="``` operator to implement backup, but that is wrong. See the example:
```javascript
var originalArray=[1,2,3,4,5];
//use "=" operators
var new1=originalArray;   
//use slice() without parameters can make a "copy"
var new2=originalArray.slice();  
//then three array all are [1,2,3,4,5], let's us do something..
new1.push(100);
new2.push(111);
//Let's look at the changes in these arrays:
console.log(new1)
console.log(new2)
console.log(originalArray)

//output:
[ 1, 2, 3, 4, 5, 100 ]
[ 1, 2, 3, 4, 5, 111 ]
[ 1, 2, 3, 4, 5, 100 ]
```
We can see that the value of the original array will be changed with the new1. Because new1 use "=" operator, just do a shortcut to the original array; The value of the original array does not change with new2. Because it uses ```slice()``` to create a new array, which has no relation to the original array.

So, we can use the ```slice()``` without the parameter to create a copy of the original array. However, if the original array is a 2D array or multidimensional arrays, the use of ```slice()``` is not enough. see example:
```javascript
var originalArray=[[1,2,3],[4,5]];
//use slice() without parameters can make a "copy"
var newarray=originalArray.slice();  
newarray[1].push(100);
//Let's look at the changes in these arrays:
console.log(newarray)
console.log(originalArray)

//output:
[ [ 1, 2, 3 ], [ 4, 5, 100 ] ]
[ [ 1, 2, 3 ], [ 4, 5, 100 ] ]
```
We can see that when the copy array is changed, the original array will be changed. How to solve this problem? When we learn another method ```map()``` will get the answer.

As a programmer, do not modify the original array is a good programming habits. In many Kata are default or explicitly pointed out: ```the user should not modify the original array```

Ok, lesson is over. let's us do some task.

## Task

Coding in function ```threeInOne```. function accept 1  parameters ```arr```, it's a 1D number array. Your task is to merge each of the 3 elements into 1 elements (sum value) and return the result. 

Note1: You should not modify the original array.

Note2: Because this is a beginner Kata, and due to the author's mercy ;-), so you do not have to verify the validity of the parameter, and do not worry about the number of elements of the array is not a multiple of 3.

Example:
```
threeInOne( [1,2,3]) should return [6]
threeInOne( [1,2,3,4,5,6]) should return [6,15]
threeInOne( [1,2,3,4,5,6,7,8,9]) should return [6,15,24]
threeInOne( [1,3,5,2,4,6,7,7,7]) should return [9,12,21]
```
    
    
## [Series](http://github.com/myjinxin2015/Katas-list-of-Training-JS-series)

( ↑↑↑ Click the link above can get my newest kata list, Please add it to your favorites)

 - [#1: create your first JS function helloWorld](http://www.codewars.com/kata/571ec274b1c8d4a61c0000c8)
 - [#2: Basic data types--Number](http://www.codewars.com/kata/571edd157e8954bab500032d)
 - [#3:  Basic data types--String](http://www.codewars.com/kata/571edea4b625edcb51000d8e)
 - [#4:  Basic data types--Array](http://www.codewars.com/kata/571effabb625ed9b0600107a)
 - [#5:  Basic data types--Object](http://www.codewars.com/kata/571f1eb77e8954a812000837)
 - [#6:  Basic data types--Boolean and conditional statements if..else](http://www.codewars.com/kata/571f832f07363d295d001ba8)
 - [#7:  if..else and ternary operator](http://www.codewars.com/kata/57202aefe8d6c514300001fd)
 - [#8: Conditional statement--switch](http://www.codewars.com/kata/572059afc2f4612825000d8a)
 - [#9: loop statement --while and do..while](http://www.codewars.com/kata/57216d4bcdd71175d6000560)
 - [#10: loop statement --for](http://www.codewars.com/kata/5721a78c283129e416000999)
 - [#11: loop statement --break,continue](http://www.codewars.com/kata/5721c189cdd71194c1000b9b)
 - [#12: loop statement --for..in and for..of](http://www.codewars.com/kata/5722b3f0bd5583cf44001000)
 - [#13: Number object and  its properties](http://www.codewars.com/kata/5722fd3ab7162a3a4500031f)
 - [#14: Methods of Number object--toString() and toLocaleString()](http://www.codewars.com/kata/57238ceaef9008adc7000603)
 - [#15: Methods of Number object--toFixed(), toExponential() and toPrecision()](http://www.codewars.com/kata/57256064856584bc47000611)
 - [#16: Methods of String object--slice(), substring() and substr()](http://www.codewars.com/kata/57274562c8dcebe77e001012)
 - [#17: Methods of String object--indexOf(), lastIndexOf() and search()](http://www.codewars.com/kata/57277a31e5e51450a4000010)
 - [#18: Methods of String object--concat() split() and its good friend join()](http://www.codewars.com/kata/57280481e8118511f7000ffa)
 - [#19: Methods of String object--toUpperCase() toLowerCase() and replace()](http://www.codewars.com/kata/5728203b7fc662a4c4000ef3)
 - [#20: Methods of String object--charAt() charCodeAt() and fromCharCode()](http://www.codewars.com/kata/57284d23e81185ae6200162a)
 - [#21: Methods of String object--trim() and the string template](http://www.codewars.com/kata/5729b103dd8bac11a900119e)
 - [#22: Unlock new skills--Arrow function,spread operator and deconstruction](http://www.codewars.com/kata/572ab0cfa3af384df7000ff8)
 - [#23: methods of arrayObject---push(), pop(), shift() and unshift()](http://www.codewars.com/kata/572af273a3af3836660014a1)
 - [#24: methods of arrayObject---splice() and slice()](http://www.codewars.com/kata/572cb264362806af46000793)
 - [#25: methods of arrayObject---reverse() and sort()](http://www.codewars.com/kata/572df796914b5ba27c000c90)
 - [#26: methods of arrayObject---map()](http://www.codewars.com/kata/572fdeb4380bb703fc00002c)
 - [#27: methods of arrayObject---filter()](http://www.codewars.com/kata/573023c81add650b84000429)
 - [#28: methods of arrayObject---every() and some()](http://www.codewars.com/kata/57308546bd9f0987c2000d07)
 - [#29: methods of arrayObject---concat() and join()](http://www.codewars.com/kata/5731861d05d14d6f50000626)
 - [#30: methods of arrayObject---reduce() and reduceRight()](http://www.codewars.com/kata/573156709a231dcec9000ee8)
 - [#31: methods of arrayObject---isArray() indexOf() and toString()](http://www.codewars.com/kata/5732b0351eb838d03300101d)
 - [#32: methods of Math---round() ceil() and floor()](http://www.codewars.com/kata/5732d3c9791aafb0e4001236)
 - [#33: methods of Math---max() min() and abs()](http://www.codewars.com/kata/5733d6c2d780e20173000baa)
 - [#34: methods of Math---pow() sqrt() and cbrt()](http://www.codewars.com/kata/5733f948d780e27df6000e33)
 - [#35: methods of Math---log() and its family](http://www.codewars.com/kata/57353de879ccaeb9f8000564)
 - [#36: methods of Math---kata author's lover:random()](http://www.codewars.com/kata/5735956413c2054a680009ec)
 - [#37: Unlock new weapon---RegExp Object](http://www.codewars.com/kata/5735e39313c205fe39001173)
 - [#38: Regular Expression--"^","$", "." and test()](http://www.codewars.com/kata/573975d3ac3eec695b0013e0)
 - [#39: Regular Expression--"?", "*", "+" and "{}"](http://www.codewars.com/kata/573bca07dffc1aa693000139)
 - [#40: Regular Expression--"|", "[]" and "()"](http://www.codewars.com/kata/573d11c48b97c0ad970002d4)
 - [#41: Regular Expression--"\"](http://www.codewars.com/kata/573e6831e3201f6a9b000971)
 - [#42: Regular Expression--(?:), (?=) and (?!)](http://www.codewars.com/kata/573fb9223f9793e485000453)
 