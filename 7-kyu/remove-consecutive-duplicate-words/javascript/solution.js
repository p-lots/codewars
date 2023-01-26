const removeConsecutiveDuplicates = (s) => {
  if (!s) {
    return "";
  }
  s = s.split(" ");
  let ret = [s[0]];
  while (typeof (_ = s.shift()) !== 'undefined') {
    if (s[0] !== ret[ret.length - 1]) {
      ret.push(s[0]);
    }
  }
  return ret.slice(0, -1).join(" ");
};
