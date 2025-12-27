const score = n => {
  return n > 1 ? 2 ** Math.ceil(Math.log2(n)) - 1 : n;
};
