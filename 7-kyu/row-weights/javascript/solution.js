const rowWeights = array => {
  const sumFunc = (arr, mod) => arr.filter((_, idx) => idx % 2 === mod).reduce((acc, nxt) => acc + nxt, 0);
  return [sumFunc(array, 0), sumFunc(array, 1)];
};
