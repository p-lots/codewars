function calculate(str) {
  const replaced = str.replace(/loses/i, "-").replace(/gains/i, "+").replace(/[^\d+-]/ig, "")
  return eval(replaced);
}