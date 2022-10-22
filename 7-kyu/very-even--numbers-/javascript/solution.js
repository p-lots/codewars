const isVeryEvenNumber = n => {
  while (n > 9) {
    n = n.toString().split("").map(num => parseInt(num)).reduce((acc, nxt) => acc + nxt, 0);
  }
  return n % 2 === 0;
};
