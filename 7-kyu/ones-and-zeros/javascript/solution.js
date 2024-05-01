const binaryArrayToNumber = arr => {
  const arrStr = arr.reduce((acc, nxt) => acc + nxt, "");
  return parseInt(arrStr, 2);
};
