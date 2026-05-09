const password = (str) => {
  const oneLetter = str.split("").some((ch) => /[a-z]/.test(ch));
  const oneUpperLetter = str.split("").some((ch) => /[A-Z]/.test(ch));
  const oneDigit = str.split("").some((ch) => /\d/.test(ch));
  return oneLetter && oneUpperLetter && oneDigit && str.length >= 8;
};
