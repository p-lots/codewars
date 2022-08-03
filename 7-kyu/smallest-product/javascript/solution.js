const smallestProduct = arr => {
  let ret = [];
  for (const subArr of arr) {
    ret.push(subArr.reduce((acc, nxt) => acc * nxt, 1));
  }
  return Math.min(...ret);
};
 