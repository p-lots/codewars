const padIt = (str, n) => {
  while (true) {
    const lhsStar = Math.ceil(n / 2);
    const rhsStar = Math.floor(n / 2);
    return `${"*".repeat(lhsStar)}${str}${"*".repeat(rhsStar)}`;
  }
};
