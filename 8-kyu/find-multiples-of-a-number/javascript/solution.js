const findMultiples = (integer, limit) => {
  let ret = [];
  for (let i = integer; i <= limit; i += integer) {
    ret.push(i);
  }
  return ret;
}
