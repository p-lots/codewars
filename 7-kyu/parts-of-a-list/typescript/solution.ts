const partlist = arr => {
  let ret = [];
  for (let i = 1; i < arr.length; i++) {
    const temp = [arr.slice(0, i).join(" "), arr.slice(i).join(" ")];
    ret.push(temp);
  }
  return ret;
};
