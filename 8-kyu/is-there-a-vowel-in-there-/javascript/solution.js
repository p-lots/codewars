const isVow = a => {
  const vowelCharCodes = [97, 101, 105, 111, 117]; // 'a', 'e', 'i', 'o', 'u'
  return a.map(elem => vowelCharCodes.includes(elem) ? String.fromCharCode(elem) : elem);
};
