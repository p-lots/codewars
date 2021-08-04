const evenLast = numbers => {
  const lastNum = numbers[numbers.length - 1];
  let ret = 0;
  for (let i = 0; i < numbers.length; i += 2) {
    ret += numbers[i] * lastNum;
  }
  return ret;
}