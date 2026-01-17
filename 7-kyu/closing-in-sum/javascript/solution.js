const closingInSum = n => {
  const nStr = n.toString();
  return [...nStr].reduce((acc, nxt, idx, arr) => {
    return idx < (nStr.length - 1) / 2 ? acc + Number(nxt + arr[arr.length - idx - 1]) : acc;
  }, 0) + nStr.length % 2 * Number(nStr[(nStr.length - nStr.length % 2) / 2]);
}
