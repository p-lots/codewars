const correct = (string) => {
  const corrections = {"5": "S", "0": "O", "1": "I"};
  return [...string].map((elem) => corrections.hasOwnProperty(elem) ? corrections[elem] : elem).join("");
};
