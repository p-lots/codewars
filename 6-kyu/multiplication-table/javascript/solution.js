const multiplicationTable = size => {
  let ret = [];
  for (let i = 1; i <= size; i++) {
    let row = [];
    for (let j = i; j <= i * size; j += i) {
      row.push(j);
    }
    ret.push(row);
  }
  return ret;
};
