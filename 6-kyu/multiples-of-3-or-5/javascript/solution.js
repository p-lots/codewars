const solution = number => {
  if (number <= 3) {
    return 0;
  }
  let ret = 0;
  for (let i = 0; i < number; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      ret += i;
    }
  }
  return ret;
};