const aliasGen = (first, last) => {
  const firstLetterAlpha = /^[a-z]/i;
  if (firstLetterAlpha.test(first) && firstLetterAlpha.test(last)) {
    return `${firstName[first[0].toUpperCase()]} ${surname[last[0].toUpperCase()]}`;
  }
  return "Your name must start with a letter from A - Z.";
};
