const noBoringZeros = n => {
  if (n === 0) {
    return 0;
  }
  let num = n;
  while (num % 10 === 0) {
    num /= 10;
  }
  return num;
};
