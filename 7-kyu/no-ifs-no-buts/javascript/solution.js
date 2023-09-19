const noIfsNoButs = (a, b) => {
  const idx = (a > b) - (a < b) + 1;
  const comparisons = ["smaller than", "equal to", "greater than"];
  const phrase = comparisons[idx];
  return `${a} is ${phrase} ${b}`;
};
