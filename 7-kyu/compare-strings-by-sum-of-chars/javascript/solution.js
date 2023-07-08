const compare = (s1, s2) => {
  const getStrSum = str => {
    if (str === null) {
      return 0;
    }
    for (const ch of str) {
      if (!ch.match(/[a-z]/gi)) {
        return 0;
      }
    }
    return [...str].reduce((acc, nxt) => acc + nxt.toUpperCase().charCodeAt(0), 0);
  };
  return getStrSum(s1) === getStrSum(s2);
};