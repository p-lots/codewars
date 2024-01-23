const pattern = n => {
  let ret = [];
  for (let i = 1; i <= n; i++) {
    ret.push(i.toString().repeat(i));
  }
  return ret.join("\n");
};
