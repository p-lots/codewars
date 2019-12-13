 A binary gap within a positive number ```num``` is any sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of  ```num```. <br/>
    For example:<br/>
    ```9``` has binary representation ```1001``` and contains a binary gap of length ```2```.<br/>
    ```529``` has binary representation ```1000010001``` and contains two binary gaps: one of length ```4``` and one of length ```3```.<br/>
    ```20``` has binary representation ```10100``` and contains one binary gap of length ```1```.<br/>
    ```15``` has binary representation ```1111``` and has ```0``` binary gaps.<br/>
    Write ```function gap(num)```
that,  given a positive ```num```,  returns the length of its longest binary gap.<br/> The function should return ```0``` if ```num``` doesn't contain a binary gap.