const solve = inputString => {
  const upperCount = (inputString.match(/[A-Z]/g) || []).length;
  const lowerCount = (inputString.match(/[a-z]/g) || []).length;
  const numberCount = (inputString.match(/[0-9]/g) || []).length;
  const specialCount = inputString.length - upperCount - lowerCount - numberCount;
  return [upperCount, lowerCount, numberCount, specialCount];
};
