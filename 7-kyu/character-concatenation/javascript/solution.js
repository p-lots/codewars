const charConcat = str => {
  let concatStr = "";
  for (let i = 0; i < Math.floor(str.length / 2); i++) {
    concatStr += `${str[i]}${str[str.length - i - 1]}${i + 1}`;
  }
  return concatStr;
};
