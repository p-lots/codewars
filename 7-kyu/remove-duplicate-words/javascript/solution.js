const removeDuplicateWords = (s) => {
  if (!s) {
    return "";
  }
  let ret = [];
  for (const word of s.split(' ')) {
    if (!ret.includes(word)) {
      ret.push(word);
    }
  }
  return ret.join(' ');
};