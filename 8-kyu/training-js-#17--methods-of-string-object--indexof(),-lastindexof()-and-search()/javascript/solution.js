const firstToLast = (str, c) => {
  if (str.search(c) === -1) {
    return -1;
  }
  return str.lastIndexOf(c) - str.indexOf(c);
};
