const flattenAndSort = array => {
  let ret = [];
  for (const subarr of array) {
    for (const n of subarr) {
      ret.push(n);
    }
  }
  return ret.sort((a, b) => a - b);
}