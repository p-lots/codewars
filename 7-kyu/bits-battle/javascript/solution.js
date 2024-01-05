const bitsBattle = numbers => {
  const odds = numbers.filter(number => number % 2 === 1).map(number => number.toString(2));
  const evens = numbers.filter(number => number % 2 === 0 && number !== 0).map(number => number.toString(2));
  const oddsOneCounts = odds.map(number => number.split("").filter(digit => digit === "1").length).reduce((acc, nxt) => acc + nxt, 0);
  const evensZeroCounts = evens.map(number => number.split("").filter(digit => digit === "0").length).reduce((acc, nxt) => acc + nxt, 0);
  return oddsOneCounts > evensZeroCounts ? "odds win" : oddsOneCounts === evensZeroCounts ? "tie" : "evens win";
};
