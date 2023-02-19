const solve = (stones) => {
  let ret = 0;
  for (let i = 0; i < stones.length - 1; i++) {
    if (stones[i] === stones[i + 1]) {
      ret += 1;
    }
  }
  return ret;
};
