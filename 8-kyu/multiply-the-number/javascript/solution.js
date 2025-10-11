const multiply = number => {
  const numDigits = number > 0 ? number.toString().length : number.toString().length - 1;
  return number * 5 ** numDigits;
};
