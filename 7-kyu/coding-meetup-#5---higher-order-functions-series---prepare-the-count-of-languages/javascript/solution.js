const countLanguages = (list) => {
  let ret = {};
  for (const obj of list) {
    if (!(ret.hasOwnProperty(obj.language))) {
      ret[obj.language] = 1;
    } else {
      ret[obj.language] += 1;
    }
  }
  return ret;
};
