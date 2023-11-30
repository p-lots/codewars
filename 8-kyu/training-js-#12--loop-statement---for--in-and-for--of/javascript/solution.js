const giveMeFive = (obj) => {
  let ret = [];
  for (const key in obj) {
    if (key.length === 5) {
      ret.push(key);
    }
    if (obj[key].length === 5) {
      ret.push(obj[key]);
    }
  }
  return ret;
}