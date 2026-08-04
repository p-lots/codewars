const threeInOne = arr => {
  const ret = [];
  for (let i = 0; i < arr.length - 2; i += 3) {
    const next3 = arr.slice(i, i + 3);
    const sum = next3.reduce((acc, nxt) => acc + nxt, 0);
    ret.push(sum);
  }
  return ret;
};
