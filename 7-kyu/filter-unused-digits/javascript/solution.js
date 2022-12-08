const unusedDigits = (...args) => {
  const allArgs = args.join("");
  const allDigits = "0123456789";
  return allDigits.split("").filter(elem => !allArgs.includes(elem)).join("");
};
