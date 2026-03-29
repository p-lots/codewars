const computerToPhone = numbers => {
  const mapping = {1: "7", 2: "8", 3: "9", 7: "1", 8: "2", 9: "3"};
  return numbers.split("").map(ch => mapping[ch] || ch).join("");
};
