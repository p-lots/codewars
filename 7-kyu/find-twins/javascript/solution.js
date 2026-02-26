const elimination = arr => {
  const count = (a, x) => a.filter(elem => elem === x).length;
  for (const n of arr) {
    if (count(arr, n) === 2) {
      return n;
    }
  }
  return null;
};
