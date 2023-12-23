const alphabetic = s => {
  for (let i = 0; i < s.length - 1; i++) {
    if (s[i].charCodeAt() > s[i + 1].charCodeAt()) {
      return false;
    }
  }
  return true;
};
