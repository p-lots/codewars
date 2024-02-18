const reverse = array => {
  let ret = JSON.parse(JSON.stringify(array));
  for (let i = array.length - 1; i >= 0; i--) {
    ret[i] = array[array.length - i - 1];
  }
  return ret;
};
