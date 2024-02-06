const encode = (str, n) => {
  const plaintextAscii = [...str].map((elem) => elem.charCodeAt(0) - "a".charCodeAt(0) + 1);
  const key = [...(n.toString())].map((elem) => parseInt(elem));
  return plaintextAscii.map((elem, i) => elem + key[i % key.length]);
};
