const sortByBit = (array) => {
  let ret = 0;
  for (const n of array) {
    ret |= (1 << n);
  }
  return ret;
};
