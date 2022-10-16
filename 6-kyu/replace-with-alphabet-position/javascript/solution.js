const alphabetPosition = (text) => {
  const asciiA = 'a'.charCodeAt(0);
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  return [...text].filter(elem => alphabet.includes(elem.toLowerCase()))
    .map(elem => (elem.toLowerCase().charCodeAt(0) - asciiA + 1).toString())
    .join(' ');
};
