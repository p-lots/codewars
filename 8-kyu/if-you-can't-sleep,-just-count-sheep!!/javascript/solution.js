const countSheep = num => {
  let ret = [];
  for (let i = 1; i <= num; i++) {
    ret.push(`${i} sheep...`);
  }
  return ret.join("");
};
