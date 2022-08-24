const highestValue = (a, b) => {
  const calculateValue = (str) => str.split("").reduce((acc, nxt) => acc + nxt.charCodeAt(0), 0);
  return calculateValue(a) >= calculateValue(b) ? a : b;
};
