# Computing the entropy of a message


## Information Theory

In information theory, entropy is a measure of the uncertainty or randomness in a message. Entropy measures the average information per symbol: higher entropy means more unpredictability. Claude Shannon defined it in 1948. The [Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) is calculated as:

```$H = - \sum p_i \cdot log_2(p_i)$```

where ```$p_i$``` is the probability of symbol ```$i$``` in the message. To calculate ```$p_i$``` count how many times each symbol appears in the message and divide by the total number of symbols. __Each unique symbol should only be considered once in the sum.__ Note: spaces are not considered as informative symbols.

For example in the message `"foo"` :
- `f` appears 1 time out of 3 symbols: ```$p_f = 1/3$```
- `o` appears 2 times out of 3 symbols: ```$p_o = 2/3$```

Thus, the entropy is: `$ -( 1/3 \cdot log_2(1/3) + 2/3 \cdot log_2(2/3) ) \approx 0.918295834 $`

[Watch a video about Shannon entropy](https://www.youtube.com/watch?v=YtebGVx-Fxw) for more context.


## Use Case

You are analyzing a collection of messages from different sources and want to determine which ones are more compressible. By calculating the entropy of each message, you can estimate their unpredictability: messages with lower entropy contain more repeated or predictable patterns and are therefore easier to compress, while messages with higher entropy are more random and less compressible. This allows you to prioritize storage or transmission strategies based on how efficiently each message can be handled.      


## Task

Write a function that receives a message (string) and returns the Shannon entropy (float) of the message.


## Notes

- Use the __math__ library for logarithm calculations
- If the message is empty, return `0.0`