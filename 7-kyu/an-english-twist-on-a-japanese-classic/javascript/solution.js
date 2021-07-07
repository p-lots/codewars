const shiritori = words => {
  if (words.length === 0)
    return [];
  let ret = [];
  let prev = words[0].slice(-1);
  if (words[0].length > 0)
    ret.push(words[0]);
  for (let i = 1; i < words.length; i++) {
    if (words[i].length === 0)
      break;
    if (words[i][0] === prev) {
      ret.push(words[i]);
    } else {
      break;
    }
    prev = words[i].slice(-1);
  }
  return ret;
};