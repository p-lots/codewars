const leastLarger = (a, i) => {
  let differences = {};
  for (let idx = 0; idx < a.length; idx++) {
    differences[idx] = a[idx] - a[i];
  }
  let ret = [-1, Number.MAX_SAFE_INTEGER];
  for (const idx in differences) {
    if (0 < differences[idx] && differences[idx] < ret[1]) {
      ret = [idx, differences[idx]];
    }
  }
  return parseInt(ret[0]);
};
