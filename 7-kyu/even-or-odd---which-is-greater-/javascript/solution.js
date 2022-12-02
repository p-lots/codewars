const evenOrOdd = str => {
  const strInt = [...str].map((elem) => parseInt(elem));
  const evenSum = strInt.filter((elem) => elem % 2 === 0).reduce((acc, nxt) => acc + nxt);
  const oddSum = strInt.filter((elem) => elem % 2 === 1).reduce((acc, nxt) => acc + nxt);
  return evenSum > oddSum ? "Even is greater than Odd" : evenSum === oddSum ? "Even and Odd are the same" : "Odd is greater than Even";
};
