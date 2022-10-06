const findOdd = A => {
  let numberCounts = {};
  for (const n of A) {
    if (!numberCounts[n]) {
      numberCounts[n] = 1;
    } else {
      numberCounts[n]++;
    }
  }
  let ret = 0;
  for (const n in numberCounts) {
    if (numberCounts[n] % 2 === 1) {
      ret = n;
      break;
    }
  }
  return parseInt(ret);
};
