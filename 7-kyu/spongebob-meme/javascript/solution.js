const spongeMeme = sentence => {
  let ret = "";
  let shouldCapitalize = true;
  for (let i = 0; i < sentence.length; i++) {
    if ((sentence[i] >= "a" && sentence[i] <= "z") || (sentence[i] >= "A" && sentence[i] <= "Z")) {
      ret += shouldCapitalize ? sentence[i].toUpperCase() : sentence[i].toLowerCase();
      if (i + 1 < sentence.length && sentence[i + 1] !== " ") {
        shouldCapitalize = !shouldCapitalize;
      }
    } else {
      ret += sentence[i];
    }
  }
  return ret;
};
