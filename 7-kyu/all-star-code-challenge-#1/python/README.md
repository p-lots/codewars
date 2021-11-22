**This Kata is intended as a small challenge for my students**

All Star Code Challenge #1

Write a function, called `sumPPG`, that takes two NBA player objects/struct/Hash/Dict/Class and sums their PPG

### Examples:

```haskell
-- Player is defined as:
data Player = Player { team :: String, ppg :: Double } deriving (Show)

iverson = Player { team = "76ers", ppg = 11.2 }
jordan  = Player { team = "bulls", ppg = 20.2 }

sumPpg iverson jordan == 31.4
```

```javascript
function NBAplayer(name, team, ppg){
  this.name=name;
  this.team=team;
  this.ppg=ppg;
}

var iverson = new NBAplayer("Iverson", "76ers", 11.2);
var jordan = new NBAplaer("Jordan", "bulls", 20.2);
sumPPG(iverson, jordan); // => 31.4
```

```python
iverson = { 'team': '76ers', 'ppg': 11.2 }
jordan =  { 'team': 'bulls', 'ppg': 20.2 }
sum_ppg(iverson, jordan) # => 31.4
```

```ruby
iverson = { "team"=>"76ers", "ppg"=> 11.2 }
jordan =  { "team"=>"bulls", "ppg"=> 20.2 }
sum_ppg(iverson, jordan) # => 31.4
```

```crystal
iverson = { "team"=>"76ers", "ppg"=> 11.2 }
jordan =  { "team"=>"bulls", "ppg"=> 20.2 }
sum_ppg(iverson, jordan) # => 31.4
```

```csharp
 Player iverson = new Player(team: "76ers", ppg: 11.2);
 Player jordan  = new Player(team: "bulls", ppg: 20.2);
 AllStars.SumPPG(iverson, jordan) // => 31.4
```

```go
iverson := NBAPlayer{ Team: "76ers", Ppg: 11.2 }
jordan  := NBAPlayer{ Team: "bulls", Ppg: 20.2 }
SumPpg(iverson,jordan) // => 31.4
```

```php
$iverson = [ 'team' => '76ers', 'ppg' => 11.2 ];
$jordan  = [ 'team' => 'bulls', 'ppg' => 20.2 ];
sumPPG($iverson, $jordan); # => 31.4
```