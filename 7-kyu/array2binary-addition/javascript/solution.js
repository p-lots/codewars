const arr2bin = (arr) => { 
  if (arr.some(elem => !Number.isInteger(elem))) {
    return false;
  }
  const sum = arr.reduce((acc, nxt) => acc + nxt, 0);
  return sum.toString(2);
};
