const pipeFix = numbers => {
  const start = Math.min(...numbers);
  const end = Math.max(...numbers);
  let ret = [];
  for (let i = start; i <= end; i++) {
    ret.push(i);
  }
  return ret;
};