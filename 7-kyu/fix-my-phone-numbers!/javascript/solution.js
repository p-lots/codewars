const isItANum = str => {
  const onlyNums = str.split("").filter(elem => /\d/.test(elem)).join("");
  if (/^0\d{10}$/.test(onlyNums)) {
    return onlyNums;
  }
  return "Not a phone number";
};
