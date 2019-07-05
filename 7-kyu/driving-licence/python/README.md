# Introduction

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="10" bgcolor="#181818">&nbsp;
    </td>
    <td bgcolor="#181818">
In the United Kingdom, the driving licence is the official document which authorises its holder to operate various types of motor vehicle on highways and some other roads to which the public have access. In England, Scotland and Wales they are administered by the Driver and Vehicle Licensing Agency (DVLA) and in Northern Ireland by the Driver & Vehicle Agency (DVA). A driving licence is required in the UK by any person driving a vehicle on any highway or other road defined in s.192 Road Traffic Act 1988[1] irrespective of ownership of the land over which the road passes, thus including many which allow the public to pass over private land; similar requirements apply in Northern Ireland under the Road Traffic (Northern Ireland) Order 1981. (Source <a href="https://en.wikipedia.org/wiki/Driving_licence_in_the_United_Kingdom">Wikipedia</a>)
    </td>
  </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
</table>

<center><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/drivinglicense.jpg" alt="Driving"></center>

# Task

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="10" bgcolor="#181818">&nbsp;
    </td>
    <td bgcolor="#181818">
The UK driving number is made up from the personal details of the driver. The individual letters and digits can be code using the below information
    </td>
  </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
</table>

# Rules

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="10" bgcolor="#181818">&nbsp;
    </td>
    <td bgcolor="#181818">
1–5: The first five characters of the surname (padded with 9s if less than 5 characters)<br><br>
6: The decade digit from the year of birth (e.g. for 1987 it would be 8)<br><br>
7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)<br><br>
9–10: The date within the month of birth<br><br>
11: The year digit from the year of birth (e.g. for 1987 it would be 7)<br><br>
12–13: The first two initials of the first name and middle name, padded with a 9 if no middle name<br><br>
14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9<br><br>
15–16: Two computer check digits. We will always use "AA"<br>
    </td>
  </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
</table>

Your task is to code a UK driving license number using an Array of data. The Array will look like

```ruby
data = ["John","James","Smith","01-Jan-2000","M"]
```
```python
data = ["John","James","Smith","01-Jan-2000","M"]
```
```javascript
data = ["John","James","Smith","01-Jan-2000","M"];
```
```csharp
data = ["John","James","Smith","01-Jan-2000","M"];
```
```c
data = {"John","James","Smith","01-Jan-2000","M"};
```
```cpp
data = {"John","James","Smith","01-Jan-2000","M"};
```
```java
data = {"John","James","Smith","01-Jan-2000","M"};
```

Where the elements are as follows
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="10" bgcolor="#181818">&nbsp;
    </td>
    <td bgcolor="#181818">
        0 = Forename<br><br>
        1 = Middle Name (if any)<br><br>
        2 = Surname<br><br>
        3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)<br><br>
        4 = M-Male or F-Female<br>
    </td>
  </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
</table>

You will need to output the full 16 digit driving license number.

Good luck and enjoy!

# Kata Series
If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td width="600"><table width="600" border="1" cellpadding="0" cellspacing="0">
      <tr>
        <td width="240"><b>Title</b></td>
        <td width="380"><b>Languages</b></td>
        <td width="66"><b>Rank</b></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/58663693b359c4a6560001d6" target="_blank">Maze Runner</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/58663693b359c4a6560001d6/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58663693b359c4a6560001d6/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58663693b359c4a6560001d6/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58663693b359c4a6560001d6/php" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/php.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58663693b359c4a6560001d6/typescript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/typescript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58663693b359c4a6560001d6/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58663693b359c4a6560001d6/typescript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/haskell.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/58693bbfd7da144164000d05" target="_blank">Scooby Doo Puzzle</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/58693bbfd7da144164000d05/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58693bbfd7da144164000d05/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58693bbfd7da144164000d05/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134" target="_blank">Driving License</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134/php" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/php.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134/c" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/typescript.png" width="30" height="30" alt="Rank" /><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/c.png" width="30" height="30" alt="Rank" /><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/cpp.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134/java" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/java.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/7KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/586c0909c1923fdb89002031" target="_blank">Connect 4</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/586c0909c1923fdb89002031/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586c0909c1923fdb89002031/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586c0909c1923fdb89002031/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586c0909c1923fdb89002031/php" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/php.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586c0909c1923fdb89002031/typescript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/typescript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586c0909c1923fdb89002031/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/5KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/586e6d4cb98de09e3800014f" target="_blank">Vending Machine</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/586e6d4cb98de09e3800014f/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586e6d4cb98de09e3800014f/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/586e6d4cb98de09e3800014f/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027" target="_blank">Snakes and Ladders</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027/php" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/php.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027/typescript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/typescript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027/cpp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/cpp.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/5KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/58a848258a6909dd35000003" target="_blank">Mastermind</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/58a848258a6909dd35000003/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58a848258a6909dd35000003/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58a848258a6909dd35000003/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/5KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/58b2c5de4cf8b90723000051" target="_blank">Guess Who?</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/58b2c5de4cf8b90723000051/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58b2c5de4cf8b90723000051/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58b2c5de4cf8b90723000051/javascript"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/58ce88427e6c3f41c2000087" target="_blank">Am I safe to drive?</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/58ce88427e6c3f41c2000087/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58ce88427e6c3f41c2000087/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58ce88427e6c3f41c2000087/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58ce88427e6c3f41c2000087/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029" target="_blank">Mexican Wave</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/javascript"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/php" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/php.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/typescript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/typescript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/crystal" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/crystal.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e" target="_blank">Pigs in a Pen</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e/php" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/php.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e/typescript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/typescript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/5KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/590300eb378a9282ba000095" target="_blank">Hungry Hippos</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/590300eb378a9282ba000095/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590300eb378a9282ba000095/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590300eb378a9282ba000095/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590300eb378a9282ba000095/php" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/php.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590300eb378a9282ba000095/typescript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/typescript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590300eb378a9282ba000095/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/5KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/5904be220881cb68be00007d" target="_blank">Plenty of Fish in the Pond</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/5904be220881cb68be00007d/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/5904be220881cb68be00007d/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/5904be220881cb68be00007d/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/5904be220881cb68be00007d/php" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/php.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/5904be220881cb68be00007d/typescript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/typescript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/5904be220881cb68be00007d/c" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/c.png" width="30" height="30" alt="Rank" /><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/cpp.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/5904be220881cb68be00007d/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/590adadea658017d90000039" target="_blank">Fruit Machine</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/590adadea658017d90000039/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590adadea658017d90000039/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590adadea658017d90000039/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590adadea658017d90000039/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590adadea658017d90000039/haskell" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/haskell.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/590adadea658017d90000039/crystal" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/crystal.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
      <tr>
        <td width="240"><a href="https://www.codewars.com/kata/591eab1d192fe0435e000014" target="_blank">Car Park Escape</a></td>
        <td width="380"><a href="https://www.codewars.com/kata/591eab1d192fe0435e000014/ruby" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/ruby.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/591eab1d192fe0435e000014/python" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/python.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/591eab1d192fe0435e000014/javascript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/javascript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/591eab1d192fe0435e000014/php" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/php.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/591eab1d192fe0435e000014/typescript" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/typescript.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/591eab1d192fe0435e000014/crystal" target="_blank"></a><a href="https://www.codewars.com/kata/591eab1d192fe0435e000014/csharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/csharp.png" width="30" height="30" alt="Rank" /></a><a href="https://www.codewars.com/kata/591eab1d192fe0435e000014/fsharp" target="_blank"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/fsharp.png" width="30" height="30" alt="Rank" /></a></td>
        <td width="66"><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/5KYU.png" width="51" height="26" alt="Rank" /></td>
      </tr>
    </table></td>
    <td>&nbsp;</td>
  </tr>
</table>
