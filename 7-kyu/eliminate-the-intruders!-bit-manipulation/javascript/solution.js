const eliminateUnsetBits = (number) => {
  const noZeroes = number.split("").filter((digit) => digit === "1").join("");
  return noZeroes.length > 0 ? parseInt(noZeroes, 2) : 0;
};
