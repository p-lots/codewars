const isSquare = n => {
  if (n < 0) {
    return false;
  }
  const root = Math.floor(n ** 0.5);
  return root * root === n;
}