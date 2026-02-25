const trailingZeros = (n) => {
  const bin = n.toString(2).split("1");
  return bin.at(-1).length;
};
