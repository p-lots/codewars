Given a string <i><b>s. </b></i>
 You have to return another string such that even-indexed and odd-indexed characters of <i><b>s</b></i> are grouped and groups are space-separated (see sample below)
<pre>
Note: 
0 is considered to be an even index. 
All input strings are valid with no spaces
</pre>
<hr>
input:
<b>'CodeWars'</b>

output
<b>'CdWr oeas'</b>
<pre>
S[0] = 'C'
S[1] = 'o'
S[2] = 'd'
S[3] = 'e'
S[4] = 'W'
S[5] = 'a'
S[6] = 'r'
S[7] = 's'
</pre>

Even indices 0, 2, 4, 6, so we have <b>'CdWr'</b> as the first group<br/>
odd ones are 1, 3, 5, 7, so the second group is <b>'oeas'</b><br/>
And the final string to return is <b>'Cdwr oeas'</b><br/>
<hr>
Enjoy.