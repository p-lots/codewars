const interlockable = (a, b) => {
  const bigger = a > b ? a : b;
  const smaller = a < b ? a : b;
  const biggerStr = bigger.toString(2);
  const smallerStr = smaller.toString(2).padStart(biggerStr.length, "0");
  for (let i = 0; i < biggerStr.length; i++) {
    if (biggerStr[i] === smallerStr[i] && biggerStr[i] === "1") {
      return false;
    }
  }
  return true;
};
