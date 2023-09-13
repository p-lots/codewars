const modifyMultiply = (str, loc, num) => {
  const strSplit = str.split(" ");
  let ret = [];
  for (let i = 0; i < num; i++) {
    ret.push(strSplit[loc]);
  }
  return ret.join("-");
};
