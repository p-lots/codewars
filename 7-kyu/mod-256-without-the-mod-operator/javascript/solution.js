const mod256WithoutMod = (number) => {
  let isNegative = false;
  if (number < 0) {
    number = Math.abs(number);
    isNegative = true;
  }
  number -= Math.floor(number / 256) * 256;
  return number * (isNegative ? -1 : 1);
};
