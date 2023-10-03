In this kata, your task is to implement an extended version of the famous rock-paper-scissors game. The rules are as follows:

* **Scissors** cuts **Paper**
* **Paper** covers **Rock**
* **Rock** crushes **Lizard**
* **Lizard** poisons **Spock**
* **Spock** smashes **Scissors**
* **Scissors** decapitates **Lizard**
* **Lizard** eats **Paper**
* **Paper** disproves **Spock**
* **Spock** vaporizes **Rock**
* **Rock** crushes **Scissors**

## Task:

~~~if-not:haskell,csharp
Given two values from the above game, return the Player result as `"Player 1 Won!"`, `"Player 2 Won!"`, or `"Draw!"`.

## Inputs

Values will be given as one of `"rock", "paper", "scissors", "lizard", "spock"`.
~~~

~~~if:haskell,csharp
Given two values from the above game, return the Player result as an `Ordering` ( `GT`, `LT` or `EQ` ).

## Inputs

Values will be given as one of `Rock, Paper, Scissors, Lizard, Spock`.
~~~


![](https://i.imgur.com/BWDszrL.jpg)
