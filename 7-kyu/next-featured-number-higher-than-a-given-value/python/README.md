Make a function that receives a value, ```val``` and outputs the smallest higher number than the given value, and this number belong to a set of positive integers that have the following properties:

- their digits occur only once

- they are odd

- they are multiple of three


```python
next_numb(12) == 15

next_numb(13) == 15

next_numb(99) == 105

next_numb(999999) == 1023459

next_number(9999999999) == "There is no possible number that
fulfills those requirements"
```
```javascript
nextNumb(12) == 15

nextNumb(13) == 15

nextNumb(99) == 105

nextNumb(999999) == 1023459

nextNumber(9999999999) == "There is no possible number that
fulfills those requirements"
```
```ruby
next_numb(12) == 15

next_numb(13) == 15

next_numb(99) == 105

next_numb(999999) == 1023459

next_number(9999999999) == "There is no possible number that fulfills those requirements"
```
```haskell
next 12         `shouldBe` Just 15           
next 13         `shouldBe` Just 15    
next 99         `shouldBe` Just 105    
next 999999     `shouldBe` Just 1023459    
next 9999999999 `shouldBe` Nothing  
```
```cpp
nextNumb(12) == 15

nextNumb(13) == 15

nextNumb(99) == 105

nextNumb(999999) == 1023459

nextNumber(9999999999) == -1 
```

Enjoy the kata!!