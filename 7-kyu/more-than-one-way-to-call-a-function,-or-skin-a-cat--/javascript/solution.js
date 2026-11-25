function sum (a, b) {
  if (arguments.length === 1) {
    const add = (c) => a + c;
    return add;
  }
  return a + b;
}