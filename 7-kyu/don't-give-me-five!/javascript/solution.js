const dontGiveMeFive = (start, end) => {
  let ret = 0;
  for (let i = start; i <= end; i++) {
    if (!(i.toString().includes('5'))) {
      ret++;
    }
  }
  return ret;
};
