const left$ = (str, i = 1) => {
  if (Number.isInteger(i)) {
    return str.slice(0, i);
  }
  return str.slice(0, str.indexOf(i));
};

const right$ = (str, i = 1) => {
  if (Number.isInteger(i)) {
    return i !== 0 ? str.slice(-i) : "";
  }
  return str.slice(str.lastIndexOf(i) + i.length);
};
