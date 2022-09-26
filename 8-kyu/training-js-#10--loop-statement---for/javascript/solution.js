const pickIt = (arr) => {
  let odd = [];
  let even = [];
  for (const n of arr) {
    if (n % 2 === 1) {
      odd.push(n);
    } else {
      even.push(n);
    }
  }
  return [odd, even];
};
