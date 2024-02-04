const createDict = (keys, values) => {
  while (values.length < keys.length) {
    values.push(null);
  }
  let obj = {};
  keys.forEach((key, idx) => obj[key] = values[idx]);
  return obj;
}