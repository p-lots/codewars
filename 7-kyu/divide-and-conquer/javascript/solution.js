const divCon = x => {
  const strings = x.filter((elem) => typeof elem === 'string').map((elem) => parseInt(elem)).reduce((acc, nxt) => acc + nxt, 0);
  const numbers = x.filter((elem) => typeof elem === 'number').reduce((acc, nxt) => acc + nxt, 0);
  return numbers - strings;
};
