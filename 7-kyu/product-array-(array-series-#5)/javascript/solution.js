const productArray = numbers => {
  const product = numbers.reduce((acc, nxt) => acc * nxt, 1);
  return numbers.map(number => product / number);
};
