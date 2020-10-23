Naming multiple files can be a pain sometimes.

#### Task:

Your job here is to create a function that will take three parameters, `fmt`, `nbr` and `start`, and create an array of `nbr` elements formatted according to `frm` with the starting index `start`. `fmt` will have `<index_no>` inserted at various locations; this is where the file index number goes in each file. 

#### Description of edge cases:

1. If `nbr` is less than or equal to 0, or not whole, return an empty array.
2. If `fmt` does not contain `'<index_no>'`, just return an array with `nbr` elements that are all equal to `fmt`. 
3. If `start` is not an integer, return an empty array.

#### What each parameter looks like:

```ruby
frm.class #=> String
  : "text_to_stay_constant_from_file_to_file <index_no>"
nbr.class #=> Fixnum
  : number_of_files
start.class #=> Fixnum
  : index_no_of_first_file
name_file(frm, nbr, start).class #=> Array(Fixnum)
```
```crystal
frm.class #=> String
  : "text_to_stay_constant_from_file_to_file <index_no>"
nbr.class #=> Int32
  : number_of_files
start.class #=> Int32
  : index_no_of_first_file
name_file(frm, nbr, start).class #=> Array(Int32)
```
```python
type(frm) #=> str
  : "text_to_stay_constant_from_file_to_file <index_no>"
type(nbr) #=> int
  : number_of_files
type(start) #=> int
  : index_no_of_first_file
type(name_file(frm, nbr, start)) #=> list
```
```javascript
typeof frm #=> 'string'
  : "text_to_stay_constant_from_file_to_file <index_no>"
typeof nbr #=> 'number'
  : number_of_files
typeof start #=> 'number'
  : index_no_of_first_file
typeof (nameFile(frm, nbr, start)) #=> 'array'
```
```coffeescript
typeof frm #=> 'string'
  : "text_to_stay_constant_from_file_to_file <index_no>"
typeof nbr #=> 'number'
  : number_of_files
typeof start #=> 'number'
  : index_no_of_first_file
typeof (nameFile(frm, nbr, start)) #=> 'array'
```

#### Some examples:

```ruby
name_file('IMG <index_no>', 4, 1)
  #=> ['IMG 1', 'IMG 2', 'IMG 3', 'IMG 4']
name_file('image #<index_no>.jpg', 3, 7)
  #=> ['image #7.jpg', 'image #8.jpg', 'image #9.jpg']
name_file('#<index_no> #<index_no>', 3, -2)
  #=> ['#-2 #-2', '#-1 #-1', '#0 #0']
```
```crystal
name_file("IMG <index_no>", 4, 1)
  #=> ["IMG 1", "IMG 2", "IMG 3", "IMG 4"])
name_file("image #<index_no>.jpg", 3, 7)
  #=> ["image #7.jpg", "image #8.jpg", "image #9.jpg"]
name_file("#<index_no> #<index_no>", 3, -2)
  #=> ["#-2 #-2", "#-1 #-1", "#0 #0"]
```
```python
name_file("IMG <index_no>", 4, 1)
  #=> ["IMG 1", "IMG 2", "IMG 3", "IMG 4"])
name_file("image #<index_no>.jpg", 3, 7)
  #=> ["image #7.jpg", "image #8.jpg", "image #9.jpg"]
name_file("#<index_no> #<index_no>", 3, -2)
  #=> ["#-2 #-2", "#-1 #-1", "#0 #0"]
```
```javascript
nameFile("IMG <index_no>", 4, 1)
  #=> ["IMG 1", "IMG 2", "IMG 3", "IMG 4"])
nameFile("image #<index_no>.jpg", 3, 7)
  #=> ["image #7.jpg", "image #8.jpg", "image #9.jpg"]
nameFile("#<index_no> #<index_no>", 3, -2)
  #=> ["#-2 #-2", "#-1 #-1", "#0 #0"]
```
```coffeescript
nameFile("IMG <index_no>", 4, 1)
  #=> ["IMG 1", "IMG 2", "IMG 3", "IMG 4"])
nameFile("image #<index_no>.jpg", 3, 7)
  #=> ["image #7.jpg", "image #8.jpg", "image #9.jpg"]
nameFile("#<index_no> #<index_no>", 3, -2)
  #=> ["#-2 #-2", "#-1 #-1", "#0 #0"]
```

Also check out my other creations — [Elections: Weighted Average](https://www.codewars.com/kata/elections-weighted-average), [Identify Case](https://www.codewars.com/kata/identify-case), [Split Without Loss](https://www.codewars.com/kata/split-without-loss), [Adding Fractions](https://www.codewars.com/kata/adding-fractions),
[Random Integers](https://www.codewars.com/kata/random-integers), [Implement String#transpose](https://www.codewars.com/kata/implement-string-number-transpose), [Implement Array#transpose!](https://www.codewars.com/kata/implement-array-number-transpose), [Arrays and Procs #1](https://www.codewars.com/kata/arrays-and-procs-number-1), and [Arrays and Procs #2](https://www.codewars.com/kata/arrays-and-procs-number-2).

If you notice any issues or have any suggestions/comments whatsoever, please don't hesitate to mark an issue or just comment. Thanks!