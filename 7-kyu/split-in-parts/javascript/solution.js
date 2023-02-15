const splitInParts = (s, partLength) => {
  let ret = [];
  for (let i = 0; i < s.length; i += partLength) {
    ret.push(s.slice(i, partLength + i));
  }
  return ret.join(' ');
};
