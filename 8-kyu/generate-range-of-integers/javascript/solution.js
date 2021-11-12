const generateRange = (min, max, step) => {
  let ret = [];
  for (let i = min; i <= max; i += step) {
    ret.push(i);
  }
  return ret;
}