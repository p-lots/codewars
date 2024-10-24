const billboard = (name, price = 30) => {
  let ret = 0;
  for (const _ of name) {
    ret += price;
  }
  return ret;
};
