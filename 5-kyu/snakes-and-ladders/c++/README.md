# Introduction

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="10" bgcolor="#181818">&nbsp;
    </td>
    <td bgcolor="#181818">
Snakes and Ladders is an ancient Indian board game regarded today as a worldwide classic. It is played between two or more players on a gameboard having numbered, gridded squares. A number of "ladders" and "snakes" are pictured on the board, each connecting two specific board squares. (Source <a href="https://en.wikipedia.org/wiki/Snakes_and_Ladders">Wikipedia</a>)
    </td>
  </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
</table>

<center><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/snakesandladders.jpg"></center>

# Task

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="10" bgcolor="#181818">&nbsp;
    </td>
    <td bgcolor="#181818">
Your task is to make a simple class called <font color="#A1A85E">SnakesLadders</font>. The test cases will call the method <font color="#A1A85E">play(die1, die2)</font> independantly of the state of the game or the player turn. The variables <font color="#A1A85E">die1</font> and <font color="#A1A85E">die2</font> are the die thrown in a turn and are both integers between 1 and 6. The player will move the sum of die1 and die2.
    </td>
  </tr>
</table>

# The Board
<img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/snakesandladdersboard.jpg">

# Rules
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="10" bgcolor="#181818">&nbsp;
    </td>
    <td bgcolor="#181818">
      1.&nbsp; There are two players and both start off the board on square 0.<br><br>
      2.&nbsp; Player 1 starts and alternates with player 2.<br><br>
      3.&nbsp; You follow the numbers up the board in order 1=>100<br><br>
      4.&nbsp; If the value of both die are the same then that player will have another go.<br><br>
      5.&nbsp; Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster. If you land exactly on a square that shows an image of the bottom of a ladder, then you may move the player all the way up to the square at the top of the ladder. (even if you roll a double).<br><br>
      6.&nbsp; Slide down snakes. Snakes move you back on the board because you have to slide down them. If you land exactly at the top of a snake, slide move the player all the way to the square at the bottom of the snake or chute. (even if you roll a double).<br><br>
      7.&nbsp; Land exactly on the last square to win. The first person to reach the highest square on the board wins. But there's a twist! If you roll too high, your player "bounces" off the last square and moves back. You can only win by rolling the exact number needed to land on the last square. For example, if you are on square 98 and roll a five, move your game piece to 100 (two moves), then "bounce" back to 99, 98, 97 (three, four then five moves.)<br>
    </td>
  </tr>
</table>


# Returns
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="10" bgcolor="#181818">&nbsp;
    </td>
    <td bgcolor="#181818">
        Return <font color="#A1A85E">Player n Wins!</font>. Where n is winning player that has landed on square 100 without any remainding moves left.<br><br>
        Return <font color="#A1A85E">Game over!</font> if a player has won and another player tries to play.<br><br>
        Otherwise return <font color="#A1A85E">Player n is on square x</font>. Where n is the current player and x is the sqaure they are currently on.<br>
    </td>
  </tr>
</table>

Good luck and enjoy!