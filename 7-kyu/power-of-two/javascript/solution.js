const isPowerOfTwo = n => {
  return n === 0 ? false : Number.isInteger(Math.log2(n));
}