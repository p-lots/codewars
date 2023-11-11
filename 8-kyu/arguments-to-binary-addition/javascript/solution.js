const arr2bin = arr => arr
  .filter(elem => typeof elem === 'number')
  .reduce((acc, nxt) => acc + nxt, 0)
  .toString(2);
