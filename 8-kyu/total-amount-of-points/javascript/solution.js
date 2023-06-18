const points = games => {
  let ret = 0;
  for (const score of games) {
    const split = score.split(":");
    if (split[0] > split[1]) {
      ret += 3;
    } else if (split[0] === split[1]) {
      ret++;
    }
  }
  return ret;
};
