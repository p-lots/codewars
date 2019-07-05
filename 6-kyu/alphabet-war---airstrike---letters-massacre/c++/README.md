# Introduction

There is a war and nobody knows - the alphabet war!  
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began. The letters called airstrike to help them in war - dashes and dots are spreaded everywhere on the battlefield.

# Task

Write a function that accepts `fight` string consists of only small letters and `*` which means a bomb drop place. Return who wins the fight after bombs are exploded. When the left side wins return `Left side wins!`, when the right side wins return `Right side wins!`, in other case return `Let's fight again!`.

The left side letters and their power:
```
 w - 4
 p - 3 
 b - 2
 s - 1
```
The right side letters and their power:
```
 m - 4
 q - 3 
 d - 2
 z - 1
```
The other letters don't have power and are only victims.  
The `*` bombs kills the adjacent letters ( i.e. `aa*aa` => `a___a`, `**aa**` => `______` );

# Example

```csharp
AlphabetWar("s*zz");           //=> Right side wins!
AlphabetWar("*zd*qm*wp*bs*"); //=> Let's fight again!
AlphabetWar("zzzz*s*");       //=> Right side wins!
AlphabetWar("www*www****z");  //=> Left side wins!
```
```javascript
alphabetWar("s*zz");           //=> Right side wins!
alphabetWar("*zd*qm*wp*bs*"); //=> Let's fight again!
alphabetWar("zzzz*s*");       //=> Right side wins!
alphabetWar("www*www****z");  //=> Left side wins!
```
```c
alphabet_war("s*zz");          /* => Right side wins!  */
alphabet_war("*zd*qm*wp*bs*"); /* => Let's fight again! */
alphabet_war("zzzz*s*");       /* => Right side wins!  */
alphabet_war("www*www****z");  /* => Left side wins!  */
```
```nasm
global main:
extern alphabet_war

section .data
strz:    db  "s*zz", 0h0
strzd:   db  "*zd*qm*wp*bs*", 0h0
strzzz:  db  "zzzz*s*", 0h0
strwww:  db  "www*www****z", 0h0

section .text
main:
    mov rdi, strz
    call alphabet_war    ; RAX <- Right side wins!
    
    mov rdi, strzd
    call alphabet_war    ; RAX <- Let's fight again!
    
    mov rdi, strzzz
    call alphabet_war    ; RAX <- Right side wins!
    
    mov rdi, strwww
    call alphabet_war    ; RAX <- Left side wins!    
    ret
```

# Alphabet war Collection

<table border="0" cellpadding="0" cellspacing="0">
<tr>
<td ><a href="https://www.codewars.com/kata/59377c53e66267c8f6000027" target="_blank">Alphavet war </a></td>
</tr>
<tr>
<td ><a href="https://www.codewars.com/kata/5938f5b606c3033f4700015a" target="_blank">Alphabet war - airstrike - letters massacre</a></td>
</tr>
<tr>
<td ><a href="https://www.codewars.com/kata/alphabet-wars-reinforces-massacre" target="_blank">Alphabet wars - reinforces massacre</a></td>
</tr>
<tr>
<td ><a href="https://www.codewars.com/kata/59437bd7d8c9438fb5000004" target="_blank">Alphabet wars - nuclear strike</a></td>
</tr>
<tr>
<td ><a href="https://www.codewars.com/kata/59473c0a952ac9b463000064" target="_blank">Alphabet war - Wo lo loooooo priests join the war</a></td>
</tr>
</table>