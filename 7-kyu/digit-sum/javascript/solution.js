const digitSum = (str) => {
  let str_n = parseInt(str);
  return str_n < 10 ? str : digitSum((Array(...str.split('')).reduce((acc, nxt) => acc + parseInt(nxt), 0)).toString());
};