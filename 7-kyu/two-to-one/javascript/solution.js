const longest = (s1, s2) => {
  const combined = s1 + s2;
  let ret = "";
  for (const ch of combined) {
    if (ret.indexOf(ch) === -1) {
      ret += ch;
    }
  }
  return ret.split('').sort().join('');
}