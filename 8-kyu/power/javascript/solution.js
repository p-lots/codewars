const numberToPower = (number, power) => {
  let ret = 1;
  for (let i = 1; i <= power; i++) {
    ret *= number;
  }
  return ret;
}
