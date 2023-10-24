const binRota = arr => {
  let ret = [];
  for (let i = 0; i < arr.length; i++) {
    if (i % 2 === 1) {
      ret.push(arr[i].reverse());
    } else {
      ret.push(arr[i]);
    }
  }
  return ret.reduce((acc, nxt) => acc.concat(nxt), []);
};
