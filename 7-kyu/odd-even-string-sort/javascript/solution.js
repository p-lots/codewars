const sortMyString = str => {
  const evenIdxChars = str.split("").filter((ch, idx) => idx % 2 === 0);
  const oddIdxChars = str.split("").filter((ch, idx) => idx % 2 === 1);
  const sortedStr = `${evenIdxChars.join("")} ${oddIdxChars.join("")}`;
  return sortedStr;
};
