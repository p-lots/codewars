const distinct = (a) => {
  let ret = [];
  for (const elem of a) {
    if (!ret.includes(elem)) {
      ret.push(elem);
    }
  }
  return ret;
};
