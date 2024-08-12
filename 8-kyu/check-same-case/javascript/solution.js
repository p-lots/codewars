const sameCase = (a, b) => {
  const islower = ch => ch.toLowerCase() === ch;
  const isupper = ch => ch.toUpperCase() === ch;
  const isalpha = ch => /^[a-z]$/i.test(ch);
  if (!isalpha(a) || !isalpha(b)) {
    return -1;
  }
  return islower(a) === islower(b) || isupper(a) === isupper(b) ? 1 : 0;
};
