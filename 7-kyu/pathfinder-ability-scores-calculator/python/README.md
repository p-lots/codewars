You've decided to try to create a test framework that allows for easy testing of [Pathfinder Ability Score](https://www.d20pfsrd.com/basics-ability-scores/ability-scores/) arrays, and their validity, using 25 points.

You will write a function that takes an array of 6 scores (integers) and will return a boolean if they add up in 25 points or less.

Each score will be in range 1 <= x <= 20.
You must comply with the table below, and values where x < 7 and x > 18 should return False.

Each score costs a certain amount of points. For example, a score of 16 costs 10 points, but a score of 7 would give 4 back.

![score table](https://db4sgowjqfwig.cloudfront.net/campaigns/145740/assets/635596/abilityScoreCosts.png?1472672582)

Python:
```python
def pathfinder_scores(scores):
```

Examples:

```python
pathfinder_scores([18, 13, 7, 12, 15, 10]) => True (Cost 25)
pathfinder_scores([13, 12, 14, 12, 15, 11]) => True (Cost 20)
pathfinder_scores([6, 19, 10, 10, 10, 10]) => False (Scores >18 and <7)
```