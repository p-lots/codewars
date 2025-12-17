const explode = x => {
  if (x.every((val) => !Number.isInteger(val))) {
    return "Void!";
  } else if (x.every((val) => Number.isInteger(val))) {
    const total = x.reduce((acc, nxt) => acc + nxt, 0);
    return Array(total).fill(x);
  }
  const repeats = x.filter((val) => Number.isInteger(val))[0];
  return Array(repeats).fill(x);
};
