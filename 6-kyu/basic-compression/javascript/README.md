<b>First, You will write a very basic compression algorithm</b>

It gets a string:<br>
<code>string="aaaaaaaabaaaa"</code><br>
And generates an array that sums all the repeating characters like so:<br>
<code>compressed=[[8,"a"],[1,"b"],[4,"a"]]</code>
<br>
The compressed version is turned into a string:<br>
<code>compressed='[[8,"a"],[1,"b"],[4,"a"]]'</code>

<b>Finally,</b><br>
If the compressed version is shorter than the original string, the function will return the compressed version.<br>
Otherwise it will return the original string. 


Example1:<br>
<code>string1="aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaa"</code><br>
<code>output1='[[26,"a"],[1,"b"],[18,"a"]]'</code><br>

Example2:<br>
<code>string2="abcde"</code><br>
<code>output2="abcde"</code><br>


After you created the compression algorithm, create a decompression algorithm:

It gets a string (output1, output2, etc.).<br>
If the string is comrpessed, it returns the uncompressed version, <br>
If it is uncompressed, it returns the original string unchanged. 

<pre><code>//output1='[[26,"a"],[1,"b"],[18,"a"]]'
uncompress(output1)
//returns
"aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaa"

//output2="abcde"
uncompress(output2)
//returns
"abcde"
</code></pre>


<b>Note:</b> The original string may not contain "[]" for obvious reasons. 



<center>
You are always welcome to check out some of my other katas:

<b>Very Easy (Kyu 8)</b>

<a href="https://www.codewars.com/kata/5926d7494b2b1843780001e6">Add Numbers</a>

<b>Easy (Kyu 7-6)</b>

<a href="https://www.codewars.com/kata/590ee3c979ae8923bf00095b">Convert Color image to greyscale</a><br>
<a href="https://www.codewars.com/kata/591190fb6a57682bed00014d">Array Transformations</a><br>
<a href="https://www.codewars.com/kata/5914e068f05d9a011e000054">Basic Compression</a><br>
<a href="https://www.codewars.com/kata/5927db23fb1f934238000015">Find Primes in Range</a><br>
<a href="https://www.codewars.com/kata/592915cc1fad49252f000006">No Ifs No Buts</a>

<b>Medium (Kyu 5-4)</b>

<a href="https://www.codewars.com/kata/5910b92d2bcb5d98f8000001">Identify Frames In An Image</a><br>
<a href="https://www.codewars.com/kata/5912950fe5bc241f9b0000af">Photoshop Like - Magic Wand</a><br>
<a href="https://www.codewars.com/kata/59255740ca72049e760000cd">Scientific Notation</a><br>
<a href="https://www.codewars.com/kata/59267e389b424dcd3f0000c9">Vending Machine - FSA</a><br>
<a href="https://www.codewars.com/kata/59293c2cfafd38975600002d">Find Matching Parenthesis</a>

<b>Hard (Kyu 3-2)</b>

<a href="https://www.codewars.com/kata/59276216356e51478900005b">Ascii Art Generator</a>
