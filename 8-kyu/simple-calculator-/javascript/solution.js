const calculator = (a, b, sign) => {
  if (/[^\+\-\*\/]/g.test(sign) || isNaN(a) || isNaN(b)) {
    return "unknown value";
  }
  if (sign === "+") {
    return a + b;
  } else if (sign === "-") {
    return a - b;
  }
  else if (sign === "*") {
    return a * b;
  } else if (sign === "/" && b !== 0) {
    return a / b;
  }
};
