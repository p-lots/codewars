const arbitrate = (input, n) => {
  for (let i = 0; i < input.length; i++) {
    if (input[i] === "1") {
      return "0".repeat(i) + "1" + "0".repeat(n - i - 1);
    }
  }
  return input;
};
