What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. `['Monday', 'Tuesday']`, `['Saturday', 'Sunday']`, `['Monday', 'Sunday']`). Week starts with Monday.

__Input:__ Year as an __int__.

__Output:__ The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

__Preconditions:__

* Week starts on Monday.
* Year is between 1583 and 4000. 
* Calendar is Gregorian.

__Example:__

```python
most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday']
```

```ruby
most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday']
```

```csharp
Kata.MostFrequentDays(2427) == {"Friday"}
Kata.MostFrequentDays(2185) == {"Saturday"}
Kata.MostFrequentDays(2860) == {"Thursday", "Friday"}
```

```javascript
mostFrequentDays(2427) => ['Friday']
mostFrequentDays(2185) => ['Saturday']
mostFrequentDays(2860) => ['Thursday', 'Friday']
```

```scala
Kata.mostFrequentDays(2427) => List("Friday")
Kata.mostFrequentDays(2185) => List("Saturday")
Kata.mostFrequentDays(2860) => List("Thursday", "Friday")
```

```java
Kata.mostFrequentDays(2427) => {"Friday"}
Kata.mostFrequentDays(2185) => {"Saturday"}
Kata.mostFrequentDays(2860) => {"Thursday", "Friday"}
```

```groovy
Kata.mostFrequentDays(2427) => ["Friday"]
Kata.mostFrequentDays(2185) => ["Saturday"]
Kata.mostFrequentDays(2860) => ["Thursday", "Friday"]
```

```fsharp
mostFrequentDays(2427) => ["Friday"]
mostFrequentDays(2185) => ["Saturday"]
mostFrequentDays(2860) => ["Thursday"; "Friday"]
```

```coffeescript
mostFrequentDays(2427) => ['Friday']
mostFrequentDays(2185) => ['Saturday']
mostFrequentDays(2860) => ['Thursday', 'Friday']
```

```vb
Kata.MostFrequentDays(2427) == {"Friday"}
Kata.MostFrequentDays(2185) == {"Saturday"}
Kata.MostFrequentDays(2860) == {"Thursday", "Friday"}
```

```go
MostFrequentDays(2427) == []string{"Friday"}
MostFrequentDays(2185) == []string{"Saturday"}
MostFrequentDays(2860) == []string{"Thursday", "Friday"}
```