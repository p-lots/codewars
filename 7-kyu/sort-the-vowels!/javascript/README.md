<h2>Sort the Vowels!</h2>

In this kata, we want to sort the vowels in a special format.

<h3>Task</h3>

Write a function which takes a input string <code>s</code> and return a string in the following way:

<pre>
<code>   
                  C|                          R|
                  |O                          n|
                  D|                          d|
   "CODEWARS" =>  |E       "Rnd Te5T"  =>      |
                  W|                          T|
                  |A                          |e
                  R|                          5|
                  S|                          T|
</code>
</pre>

Notes:

<ul>
<li>List all the Vowels on the right side of <code>|</code></li>
<li>List every character except Vowels on the left side of <code>|</code></li>
<li>for the purpose of this kata, the vowels are : <code>a e i o u</code></li>
<li>Return every character in its original case</li>
<li>Each line is seperated with <code>\n</code></li>
<li>Invalid input <code>( undefined / null / integer )</code> should return an empty string</li>
</ul>