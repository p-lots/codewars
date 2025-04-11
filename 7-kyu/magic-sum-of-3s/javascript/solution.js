const magicSum = numbers => {
  const reducer = (acc, nxt) => acc + (nxt.toString().includes("3") && nxt % 2 === 1 ? nxt : 0);
  return numbers.reduce(reducer, 0);
};
