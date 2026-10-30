const solution = (first, second) => {
  let a = Math.max(first, second);
  let b = Math.min(first, second);
  let c = a - b;
  if (c > b) {
    return [b, a];
  }
  const allTerms = [a, b, c];
  while (c >= 0) {
    a = b;
    b = c;
    c = a - b;
    allTerms.push(a);
  }
  return allTerms.reverse().slice(0, 2);
};
