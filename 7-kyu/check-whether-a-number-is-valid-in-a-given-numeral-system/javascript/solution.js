const validateBase = (num, base) => {
  const bases = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  return num.toString().split("").every(digit => bases.indexOf(digit) < base);
};
