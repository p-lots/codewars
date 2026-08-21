const spEng = sentence => {
  const engRegExp = /english/ig;
  return engRegExp.test(sentence);
};
