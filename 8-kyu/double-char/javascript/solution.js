const doubleChar = (str) => {
  let ret = "";
  for (const ch of str) {
    ret += ch.repeat(2);
  }
  return ret;
};
