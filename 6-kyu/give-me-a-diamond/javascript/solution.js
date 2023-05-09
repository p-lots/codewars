const diamond = (n) => {
  if (n % 2 === 0 || n < 1) {
    return null;
  }
  if (n === 1) {
    return "*\n";
  }
  let ret = [];
  let spacesBefore = Math.floor(n / 2);
  let asterisks = 1;
  for (let i = 0; i < n; i++) {
    let line = "";
    if (i < (n - 1) / 2) {
      line = " ".repeat(spacesBefore) + "*".repeat(asterisks);
      ret.push(line);
      spacesBefore--;
      asterisks += 2;
    } else if (i === (n - 1) / 2) {
      line = "*".repeat(n);
      ret.push(line);
      spacesBefore = 1;
      asterisks -= 2;
    } else {
      line = " ".repeat(spacesBefore) + "*".repeat(asterisks);
      ret.push(line);
      spacesBefore++;
      asterisks -= 2;
    }
  }
  return ret.join("\n") + "\n";
}
