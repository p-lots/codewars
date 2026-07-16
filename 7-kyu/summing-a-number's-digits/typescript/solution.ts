const sumDigits = number => {
  return Math.abs(number)
    .toString()
    .split("")
    .reduce((acc, nxt) => acc + parseInt(nxt), 0);
};
