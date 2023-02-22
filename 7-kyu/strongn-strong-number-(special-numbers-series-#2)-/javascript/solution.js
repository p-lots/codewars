const fact = (number) => {
  if (number === 0) {
    return 1;
  } else if (number <= 2) {
    return number;
  }
  let ret = 1;
  for (let i = 2; i <= number; i++) {
    ret *= i;
  }
  return ret;
};

const strong = (n) => {
  const ret = [...(n.toString())].map((elem) => fact(parseInt(elem))).reduce((acc, nxt) => acc + parseInt(nxt), 0);
  return ret === n ? "STRONG!!!!" : "Not Strong !!";
};
