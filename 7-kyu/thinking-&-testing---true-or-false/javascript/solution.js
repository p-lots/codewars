const testit = n => n.toString(2)
  .split("")
  .filter(digit => digit === "1")
  .length;
