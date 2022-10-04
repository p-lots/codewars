const createPhoneNumber = (numbers) => {
  const areaCode = numbers.slice(0, 3).join("");
  const firstPartOfNumber = numbers.slice(3, 6).join("");
  const lastPartOfNumber = numbers.slice(6).join("");
  return `(${areaCode}) ${firstPartOfNumber}-${lastPartOfNumber}`;
};
