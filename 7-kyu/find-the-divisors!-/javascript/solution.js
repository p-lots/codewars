const divisors = integer => {
  let ret = [];
  for (let i = 2; i < integer; i++) {
    if (integer % i === 0) {
      ret.push(i);
    }
  }
  return ret.length !== 0 ? ret : `${integer} is prime`;
};
