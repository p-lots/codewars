const maxedOut = arr => {
  const sum = arr.map(num => num ** 3).reduce((acc, nxt) => acc + nxt, 0)
  return Number.isSafeInteger(sum) ? sum : "You've pushed me to the max!";
};
