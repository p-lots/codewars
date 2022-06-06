const trouble = (x, t) => {
  let ret = [x[0]];
  for (let i = 1; i < x.length; i++) {
    const retLastIdx = ret.length - 1;
    if (ret[retLastIdx] + x[i] !== t) {
      ret.push(x[i]);
    }
  }
  return ret;
};
