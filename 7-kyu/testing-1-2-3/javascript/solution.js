const number = (array) => {
  if (!array) {
    return [];
  }
  let i = 1;
  let ret = [];
  for (const elem of array) {
    ret.push(`${i++}: ${elem}`);
  }
  return ret;
};
