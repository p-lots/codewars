Makes the Sentence:

You are to write a function that is passed 2 arguments and should return a boolean true or false.

The first argument is an array of characters, where each index will contain  either a lowercase character from a-z, an uppercase characters from A-Z, or one of the charcters '.', '?', or '!'.

An example array is: ['D', 'u', 'c', 'k', 's', 'q', 'u', 'a', 'c', 'k', '.']

The second argument passed to your function is a string that is a grammatically correct complete English sentence composed of only  the charcters a-z, A-Z, '.', '?', '!', and white spaces.

An example string is: "Ducks quack."

Your function should return true if the sentence string can be constructed using only the characters in the array passed in (each character can only be used once) and any amout of needed white spaces, otherwise it should return false.

Since each character can only be used once, the count of each character in the passed in character array should match the count of each character in the passed in sentence string so:

makesTheSentence(['S', 'h', 'e', 'a', 'd', 's', '.'], "She adds.");

Should return false because there is only 1 'd' in the passed in array and there are 2 'd's in the passed in string.

<!-- C# documentation -->
```if:csharp
<h1>Documentation:</h1>
<h2>Kata.MakesTheSentence Method (List&lt;Char&gt;, String)</h2>

Returns a boolean representing if the second argument can be composed of the characters from the first, excluding whitespaces.

<span style="font-size:20px">Syntax</span>
<div style="margin-top:-10px;padding:1px;background-color:Grey;position:relative;left:20px;width:600px;">
  <div style="background-color:White;color:Black;border:1px;display:block;padding:10px;padding-left:18px;font-family:Consolas,Courier,monospace;">
    <span style="color:Blue;">public</span>
    <span style="color:Blue;">static</span>
    <span style="color:Blue;">bool</span> MakesTheSentence(</br>
    <span style="position:relative;left:62px;">List&lt;<span style="color:Blue;">char</span>&gt; characters,</span></br>
    <span style="position:relative;left:62px;"><span style="color:Blue;">string</span> sentence</span></br>
    )
  </div>
</div>
</br>
<div style="position:relative;left:20px;">
  <strong>Parameters</strong>
  </br>
  <i>characters</i>
  </br>
  <span style="position:relative;left:50px;">Type: <a href="https://msdn.microsoft.com/en-us/library/6sh2ey19(v=vs.110).aspx">System.Collections.Generic.List&lt;char&gt;</a></span></br>
  <span style="position:relative;left:50px;">The list of characters.</span>
  </br></br>
  <i>sentence</i>
  </br>
  <span style="position:relative;left:50px;">Type: <a href="https://msdn.microsoft.com/en-us/library/system.string(v=vs.110).aspx">System.String</a></span></br>
  <span style="position:relative;left:50px;">The sentence to compare against.</span>
  </br></br>
  <strong>Return Value</strong>
  </br>
  <span>Type: <a href="https://msdn.microsoft.com/en-us/library/system.boolean(v=vs.110).aspx">System.Boolean</a></span></br>
  <strong>True</strong> if <i>sentence</i> can be made up of characters from <i>characters</i> else <strong>false</strong>.
</div>
```
<!-- end C# documentation -->