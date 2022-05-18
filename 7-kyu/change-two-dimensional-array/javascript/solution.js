const matrix = array => {
  let ret = JSON.parse(JSON.stringify(array));
  for (let i = 0; i < ret.length; i++) {
    if (ret[i][i] < 0) {
      ret[i][i] = 0;
    } else {
      ret[i][i] = 1;
    }
  }
  return ret;
};