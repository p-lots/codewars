const comes_after = (str, letter) => {
  let ret = "";
  str.split("").forEach((ch, idx) => {
    if (ch.toLowerCase() === letter && idx + 1 < str.length && /[a-z]/ig.test(str[idx + 1])) {
      ret += str[idx + 1];
    }
  })
  return ret;
};
