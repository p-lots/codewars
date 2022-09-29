const fiveLine = (s) => {
  s = s.trim();
  let ret = [];
  for (let i = 1; i <= 5; i++) {
    ret.push(`${s.repeat(i)}`);
  }
  return ret.join("\n");
};
