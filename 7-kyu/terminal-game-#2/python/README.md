## Create the hero move method

Create a move method for your hero to move through the level.

Adjust the hero's position by changing the `position` attribute. The level is a grid with the following values:

<style>
  .grid {
    width: 20em;
    }
  .grid tr, td {
    border: 2px solid grey;
    }
  .grid td {
    text-align: center; 
    vertical-align: middle;
  }
</style>
<table class = "grid">
  <tr>
    <td>00</td>
    <td>01</td>
    <td>02</td>
    <td>03</td>
    <td>04</td>
  </tr>
  <tr>
    <td>10</td>
    <td>11</td>
    <td>12</td>
    <td>13</td>
    <td>14</td>
  </tr>
  <tr>
    <td>20</td>
    <td>21</td>
    <td>22</td>
    <td>23</td>
    <td>24</td>
  </tr>
  <tr>
    <td>30</td>
    <td>31</td>
    <td>32</td>
    <td>33</td>
    <td>34</td>
  </tr>
  <tr>
    <td>40</td>
    <td>41</td>
    <td>42</td>
    <td>43</td>
    <td>44</td>
  </tr>
</table><p>

The `dir` argument will be a string 
```
up
down
left
right
```
If the position is not inside the level grid the method should throw an error and not move the hero