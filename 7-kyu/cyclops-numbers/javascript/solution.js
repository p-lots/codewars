const cyclops = n => {
  const nBin = n.toString(2);
  const cyclopsRegex = /^(1+)0\1$/g;
  return cyclopsRegex.test(nBin);
};
