const orderFood = (list) => {
  let ret = {};
  for (const obj of list) {
    if (!ret.hasOwnProperty(obj.meal)) {
      ret[obj.meal] = 1;
    } else {
      ret[obj.meal]++;
    }
  }
  return ret;
};
