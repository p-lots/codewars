const sequenceSum = (begin, end, step) => {
  let ret = 0;
  for (let i = begin; i <= end; i += step) {
    ret += i;
  }
  return ret;
};