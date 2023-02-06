const findShort = (s) => {
  const ret = s.split(" ").map((elem) => elem.length);
  return Math.min(...ret);
};
