const solve = (a, b) => {
  const aSet = new Set(a);
  const bSet = new Set(b);
  return a.split("").filter(ch => !bSet.has(ch)).join("") + b.split("").filter(ch => !aSet.has(ch)).join("");
};
