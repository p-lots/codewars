const prevMultOfThree = n => {
  n = n.toString();
  while (n) {
    if (parseInt(n) % 3 === 0) {
      return parseInt(n);
    }
    n = n.slice(0, -1);
  }
  return null;
};
