const stringy = size => {
  let ret = "";
  for (let i = 0; i < size; i++) {
    ret += (i % 2 === 0 ? "1" : "0");
  }
  return ret;
}