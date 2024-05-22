const separateTypes = (input) => {
  let ret = {};
  for (const elem of input) {
    const type = typeof elem;
    if (ret.hasOwnProperty(type)) {
      ret[type].push(elem);
    } else {
      ret[type] = [elem];
    }
  }
  return ret;
};
