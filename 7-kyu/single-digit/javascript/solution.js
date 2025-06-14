function singleDigit(n) {
  if (n.toString().length === 1) {
    return n;
  }
  const bin = n.toString(2);
  const sum = bin.split("").reduce((acc, nxt) => acc + Number(nxt), 0);
  return singleDigit(sum);
}