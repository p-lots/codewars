const calculate = (a, operator, b) => {
  switch (operator) {
      case "+":
      return a + b;
      break;
      case "-":
      return a - b;
      break;
      case "*":
      return a * b;
      break;
      case "/":
      if (b === 0) return null;
      return a / b;
      break;
      default:
      return null;
      break;
  }
  return null;
};
