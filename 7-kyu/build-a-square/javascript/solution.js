const generateShape = integer => {
  let ret = "";
  for (let i = 0; i < integer; i++) {
    for (let j = 0; j < integer; j++) {
      ret += "+";
    }
    if (i < integer - 1) {
      ret += "\n";
    }
  }
  return ret;
}