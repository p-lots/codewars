const isConsecutive = str => {
  const seen = [];
  for (let i = 0; i < str.length; i++) {
    if (!seen.includes(str[i])) {
      seen.push(str[i]);
    } else {
      let j = i;
      while (str[j] === str[i]) {
        j++;
      }
      if (j !== str.lastIndexOf(str[i]) + 1) {
        return false;
      }
    }
  }
  return true;
};
