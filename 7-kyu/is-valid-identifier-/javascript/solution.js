const isValid = idn => {
  const validRegex = /^[a-z_\$][a-z0-9_\$]*$/gi;
  return validRegex.test(idn);
};
