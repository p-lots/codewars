const addLetters = (...letters) => {
  if (letters.length === 0) {
    return 'z';
  }
  let total = letters.reduce((accum, letter) => {
    const charCode = letter.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
    return accum + charCode;
  }, 0);
  if (total % 26 === 0) {
    return 'z';
  }
  return String.fromCharCode(total % 26 + 'a'.charCodeAt(0) - 1);
};
