Linked Lists - Get Nth

Implement a GetNth() function that takes a linked list and an integer index and returns the node stored at the Nth index position. GetNth() uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on. So for the list 42 -> 13 -> 666, GetNth() with index 1 should return Node(13);

```javascript
getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2
```
```csharp
Node.GetNth(1 -> 2 -> 3 -> null, 0).Data == 1
Node.GetNth(1 -> 2 -> 3 -> null, 1).Data == 2
```

The index should be in the range [0..length-1]. If it is not, GetNth() should throw/raise an exception (`ArgumentException` in C#, `InvalidArgumentException` in PHP). You should also raise an exception (`ArgumentException` in C#, `InvalidArgumentException` in PHP) if the list is empty/null/None.


Prerequisite Kata (may be in beta):

- <a href="http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree">Linked Lists - Push & BuildOneTwoThree</a>
- <a href="http://www.codewars.com/kata/linked-lists-length-and-count">Linked Lists - Length & Count</a>

> The push() and buildOneTwoThree() (`BuildOneTwoThree` in C#, `build_one_two_three()` in PHP) functions do not need to be redefined.

**Related Kata in order of expected completion (increasing difficulty):**

- <a href="http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree">Linked Lists - Push & BuildOneTwoThree</a>
- <a href="http://www.codewars.com/kata/linked-lists-length-and-count">Linked Lists - Length & Count</a>
- <a href="http://www.codewars.com/kata/linked-lists-get-nth-node">Linked Lists - Get Nth Node</a>
- <a href="http://www.codewars.com/kata/linked-lists-insert-nth-node">Linked Lists - Insert Nth Node</a>
- <a href="http://www.codewars.com/kata/linked-lists-sorted-insert">Linked Lists - Sorted Insert</a><br>
- <a href="http://www.codewars.com/kata/linked-lists-insert-sort">Linked Lists - Insert Sort</a>
- <a href="http://www.codewars.com/kata/linked-lists-append">Linked Lists - Append</a>
- <a href="http://www.codewars.com/kata/linked-lists-remove-duplicates">Linked Lists - Remove Duplicates</a>
- <a href="http://www.codewars.com/kata/linked-lists-move-node">Linked Lists - Move Node</a>
- <a href="http://www.codewars.com/kata/linked-lists-move-node-in-place">Linked Lists - Move Node In-place</a>
- <a href="http://www.codewars.com/kata/linked-lists-alternating-split">Linked Lists - Alternating Split</a>
- <a href="http://www.codewars.com/kata/linked-lists-front-back-split">Linked Lists - Front Back Split</a>
- <a href="http://www.codewars.com/kata/linked-lists-shuffle-merge">Linked Lists - Shuffle Merge</a>
- <a href="http://www.codewars.com/kata/linked-lists-sorted-merge">Linked Lists - Sorted Merge</a>
- <a href="http://www.codewars.com/kata/linked-lists-merge-sort">Linked Lists - Merge Sort</a>
- <a href="http://www.codewars.com/kata/linked-lists-sorted-intersect">Linked Lists - Sorted Intersect</a>
- <a href="http://www.codewars.com/kata/linked-lists-iterative-reverse">Linked Lists - Iterative Reverse</a>
- <a href="http://www.codewars.com/kata/linked-lists-recursive-reverse">Linked Lists - Recursive Reverse</a>


Inspired by Stanford Professor Nick Parlante's excellent [Linked List teachings.](http://cslibrary.stanford.edu/103/LinkedListBasics.pdf)

http://cslibrary.stanford.edu/103/LinkedListBasics.pdf<br>
http://cslibrary.stanford.edu/105/LinkedListProblems.pdf
