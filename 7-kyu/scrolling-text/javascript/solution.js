const scrollingText = (text) => {
  let ret = [text.toUpperCase()];
  for (let i = 0; i < text.length - 1; i++) {
    ret.push(text.toUpperCase().slice(i + 1) + text.toUpperCase().slice(0, i + 1));
  }
  return ret;
};
