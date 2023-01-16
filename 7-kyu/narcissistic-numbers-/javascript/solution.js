const isNarcissistic = n => {
  const len = n.toString().length;
  const ret = n.toString().split("").map(elem => parseInt(elem) ** len).reduce((acc, nxt) => acc + nxt, 0);
  return ret === n;
};
