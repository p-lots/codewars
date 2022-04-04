const sumStr = (a, b) => {
  let aInt = parseInt(a);
  if (!aInt) {
    aInt = 0;
  }
  let bInt = parseInt(b);
  if (!bInt) {
    bInt = 0;
  }
  const result = aInt + bInt;
  return result.toString();
}
